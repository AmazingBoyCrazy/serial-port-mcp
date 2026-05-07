---
name: serial-port-mcp
description: >
  串口设备调试助手。当用户需要通过串口连接设备、发送 AT 命令、读取设备数据、
  执行设备上的 shell 命令（如 cd、./app）、获取 SylixOS/Linux 设备返回信息时触发。
  涉及串口通信、串口调试、COM 口操作、设备命令执行都应该使用此技能。
  串口 MCP Server 位于 E:/650IDE/workspace/18ws_100tai/mcp_serial_server/serial_mcp_server.py，
  已在 ~/.claude/.mcp.json 中全局配置，新会话中 mcp 工具已自动就绪。
---

# Serial Port MCP 助手

本 MCP 提供串口通信能力，用于连接嵌入式设备（SylixOS、Linux 等）并执行命令。

## 前提条件

- MCP Server 已在 `~/.claude/.mcp.json` 中配置
- 目标设备的串口已连接到 PC（如 COM54、COM55 等 USB-SERIAL 端口）
- pyserial 和 mcp 库已安装：`pip install pyserial mcp`

## 可用工具

| 工具 | 功能 | 关键参数 |
|------|------|----------|
| `list_ports` | 列出 PC 所有可用串口 | 无 |
| `open_port` | 打开指定串口 | `port` (如 "COM55")，`baudrate` (默认 115200)，`timeout` (默认 1.0) |
| `close_port` | 关闭当前串口 | 无 |
| `read_data` | 从串口读取数据 | `size` (默认 1024) |
| `write_data` | 向串口发送数据 | `data` (字符串)，`encoding` (默认 utf-8) |
| `get_status` | 获取连接状态 | 无 |

## 典型工作流

### 1. 列出可用串口

```
mcp__serial-port__list_ports
```

找到目标设备对应的 COM 口（如 COM55）。

### 2. 打开串口

```
mcp__serial-port__open_port --port "COM55" --baudrate 115200 --timeout 2.0
```

### 3. 发送命令并读取返回

```
# 切换目录
mcp__serial-port__write_data --data "cd /apps/helloworld\n"
mcp__serial-port__read_data

# 执行程序
mcp__serial-port__write_data --data "./helloworld\n"
mcp__serial-port__read_data
```

**注意**：命令通常需要 `\n` 换行符结尾，设备才会执行。

### 4. 关闭串口

```
mcp__serial-port__close_port
```

---

# SylixOS Shell 命令参考

> **重要**：SylixOS 是实时操作系统，不是 Linux，shell 命令与 Linux 有差异。
> 详细命令参考：[SylixOS_Shell_Reference.md](./SylixOS_Shell_Reference.md)

## SylixOS vs Linux 主要区别

| 特性 | SylixOS | Linux |
|------|---------|-------|
| 标准目录 | `/apps`, `/bin`, `/etc`, `/root` | `/bin`, `/usr`, `/proc`, `/sys` |
| 网络配置 | `ifconfig` | `ip addr` |
| 进程查看 | `ps`, `top` | `ps`, `top` |
| 模块加载 | `insmod`/`lsmod`/`rmmod` | 相同 |

## 常用命令速查

### 文件/目录操作

| 命令 | 功能 | 示例 |
|------|------|------|
| `ls` | 列出目录文件 | `ls`, `ls /apps` |
| `ll` | 详细列表 | `ll -l /apps` |
| `cd` | 切换目录 | `cd /apps/helloworld` |
| `pwd` | 显示当前目录 | `pwd` |
| `mkdir` | 创建目录 | `mkdir /apps/test` |
| `cat` | 显示文件内容 | `cat /etc/rc.conf` |
| `cp` | 复制文件 | `cp /bin/app /apps/` |
| `rm` | 删除文件 | `rm /apps/test/file` |

### 进程/线程管理

| 命令 | 功能 | 示例 |
|------|------|------|
| `ps` | 查看进程 | `ps` |
| `top` | CPU 使用率 | `top` |
| `kill` | 发送信号 | `kill <pid>`, `kill -9 <pid>` |
| `killall` | 按名杀进程 | `killall appname` |
| `sleep` | 线程睡眠 | `sleep 5` |
| `restart` | 重启进程 | `restart <pid>` |

### 网络命令

| 命令 | 功能 | 示例 |
|------|------|------|
| `ifconfig` | 网卡配置 | `ifconfig`, `ifconfig eth0` |
| `ping` | 网络测试 | `ping 192.168.1.1` |
| `netstat` | 网络状态 | `netstat -a` |

### 内存/存储

| 命令 | 功能 | 示例 |
|------|------|------|
| `free` | 内存信息 | `free` |
| `df` | 文件系统 | `df -h` |

### 系统命令

| 命令 | 功能 | 示例 |
|------|------|------|
| `reboot` | 重启 | `reboot` |
| `shutdown` | 关机 | `shutdown` |
| `date` | 日期时间 | `date` |
| `help` | 帮助 | `help`, `help <command>` |

### 模块加载

| 命令 | 功能 | 示例 |
|------|------|------|
| `insmod` | 加载模块 | `insmod /lib/drivers/drv.ko` |
| `lsmod` | 查看模块 | `lsmod` |
| `rmmod` | 卸载模块 | `rmmod drv` |

## SylixOS 常用工作流

### 1. 进入目录执行程序
```
cd /apps/helloworld
./helloworld
```

### 2. 查看系统资源
```
free          # 内存
df -h         # 磁盘
cpuus         # CPU 使用统计
top           # 实时监控
```

### 3. 网络测试
```
ifconfig      # 查看 IP
ping 192.168.1.1
netstat -a    # 查看连接
```

### 4. 进程管理
```
ps            # 查看进程
kill <pid>    # 杀进程
restart <pid> # 重启
```

### 5. 获取设备帮助
```
help          # 所有命令
help ps       # 特定命令
```

---

## 故障排查

| 问题 | 解决方法 |
|------|----------|
| `PermissionError` 端口被占用 | 关闭其他串口软件（串口调试助手、Arduino IDE 等） |
| 读不到数据 | 增加 `timeout` 值，或检查设备波特率是否匹配 |
| 返回乱码 | 尝试不同的 `baudrate`（9600、57600、115200） |
| 命令无响应 | 设备可能需要 `\r\n` 换行符，而非仅 `\n` |
| 目录不存在 | SylixOS 目录可能是 `/apps/` 而非 `/bin/` |
| 命令不存在 | 使用 `help` 查看可用命令，SylixOS 与 Linux 命令有差异 |

## 工具调用示例

完整调用示例（在对话中让 agent 执行）：

```
请使用 serial-port MCP：
1. 打开 COM55，波特率 115200
2. 发送命令 "cd /apps/helloworld" 然后发送 "./helloworld"
3. 读取并返回设备输出
4. 关闭串口
```

## 设备登录后的典型输出

SylixOS 设备登录后显示：
```
[root@sylixos:/apps/helloworld]#
```

格式：`[用户名@设备名:当前目录]#`
