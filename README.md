# sylixos Serial Port MCP 快速上手指南

本仓库提供基于 Model Context Protocol (MCP) 的串口通信能力，可连接 SylixOS/Linux 嵌入式设备进行调试。
提供SylixOS shell 命令概览，协助 SylixOS 通过串口进行调试。

---

## 目录结构

```
serial-port-mcp/
├── mcp_serial_server/           # MCP Server
│   ├── serial_mcp_server.py     # 主程序
│   ├── requirements.txt         # 依赖
│   ├── list_ports.py            # 串口检测脚本
│   └── execute_on_device.py     # 执行脚本
├── serial-port-mcp/             # Claude Code Skill
│   ├── SKILL.md                 # 技能说明
│   ├── AGENTS.md                # Agent 使用指南
│   └── SylixOS_Shell_Reference.md # SylixOS 命令参考
└── README.md # 本文档
```

---

## 第一步：安装依赖

```bash
pip install pyserial mcp
```

---

## 第二步：注册 MCP Server

### 方法一：全局注册（推荐）

创建或编辑 `~/.claude/.mcp.json` 文件：

```json
{
  "mcpServers": {
    "serial-port": {
      "command": "python",
      "args": ["<仓库路径>/mcp_serial_server/serial_mcp_server.py"]
    }
  }
}
```

**Windows 示例**：
```json
{
  "mcpServers": {
    "serial-port": {
      "command": "python",
      "args": ["E:/projects/serial-port-mcp/mcp_serial_server/serial_mcp_server.py"]
    }
  }
}
```

**Linux/macOS 示例**：
```json
{
  "mcpServers": {
    "serial-port": {
      "command": "python3",
      "args": ["/home/user/serial-port-mcp/mcp_serial_server/serial_mcp_server.py"]
    }
  }
}
```

### 方法二：项目级注册

在项目根目录创建 `.mcp.json`：

```json
{
  "mcpServers": {
    "serial-port": {
      "command": "python",
      "args": ["./mcp_serial_server/serial_mcp_server.py"]
    }
  }
}
```

### 验证 MCP Server

启动 Claude Code 后，运行以下命令测试：

```
mcp__serial-port__list_ports
```

如果返回可用串口列表，说明注册成功。

---

## 第三步：注册 Skill

### 全局 Skill（所有项目可用）

将 `serial-port-mcp` 目录复制到 `~/.claude/skills/`：

```bash
# Windows
xcopy /E /I <仓库路径>\serial-port-mcp C:\Users\<用户名>\.claude\skills\serial-port-mcp

# Linux/macOS
cp -r <仓库路径>/serial-port-mcp ~/.claude/skills/
```

### 项目级 Skill（仅当前项目可用）

将 `serial-port-mcp` 目录复制到项目 `.claude/skills/`：

```bash
# Windows
xcopy /E /I <仓库路径>\serial-port-mcp <项目路径>\.claude\skills\serial-port-mcp

# Linux/macOS
cp -r <仓库路径>/serial-port-mcp <项目路径>/.claude/skills/
```

**项目级目录结构**：
```
your-project/
├── .claude/
│   └── skills/
│       └── serial-port-mcp/
│           ├── SKILL.md
│           ├── AGENTS.md
│           └── SylixOS_Shell_Reference.md
├── src/
└── ...
```

---

## 第四步：使用串口调试

### 1. 列出可用串口

```
mcp__serial-port__list_ports
```

### 2. 打开串口

```
mcp__serial-port__open_port --port "COM55" --baudrate 115200 --timeout 2.0
```

### 3. 发送命令

```
mcp__serial-port__write_data --data "cd /apps/helloworld\n"
mcp__serial-port__read_data

mcp__serial-port__write_data --data "./helloworld\n"
mcp__serial-port__read_data
```

### 4. 关闭串口

```
mcp__serial-port__close_port
```

---

## 可用 MCP 工具

| 工具 | 功能 | 关键参数 |
|------|------|----------|
| `list_ports` | 列出所有可用串口 | 无 |
| `open_port` | 打开串口 | `port` (如 "COM55")，`baudrate` (默认 115200) |
| `close_port` | 关闭串口 | 无 |
| `read_data` | 读取数据 | `size` (默认 1024) |
| `write_data` | 发送数据 | `data` (字符串) |
| `get_status` | 获取连接状态 | 无 |

---

## 常见问题

### Q: 端口被占用
**A**: 关闭其他串口软件（串口调试助手、Arduino IDE 等）

### Q: 读不到数据
**A**: 增加 `timeout` 值，或检查设备波特率

### Q: 返回乱码
**A**: 尝试不同波特率（9600、57600、115200）

### Q: 命令无响应
**A**: SylixOS 设备需要 `\n` 换行符结尾

---

## SylixOS vs Linux Shell 差异

| 特性 | SylixOS | Linux |
|------|---------|-------|
| 标准目录 | `/apps`, `/bin`, `/etc` | `/bin`, `/usr`, `/proc` |
| 网络配置 | `ifconfig` | `ip addr` |
| 帮助命令 | `help` | `help` 或 `man` |

详细命令参考：[SylixOS_Shell_Reference.md](./serial-port-mcp/SylixOS_Shell_Reference.md)

---

## 相关链接

- [SylixOS 官方文档](https://docs.acoinfo.com/sylixos/shell/)
