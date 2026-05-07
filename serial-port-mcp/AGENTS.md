# Serial Port MCP 使用指南

## 触发场景

当遇到以下任务时，应该调用 serial-port-mcp：

1. **串口设备调试** - 需要连接设备、发送命令、读取返回
2. **嵌入式设备交互** - 与 SylixOS/Linux 设备通过串口通信
3. **AT 命令调试** - 发送 AT 指令到模块（模组、Modem 等）
4. **设备 shell 操作** - 通过串口在设备上执行 shell 命令
5. **获取设备信息** - 读取设备串口输出、日志、状态

## 快速开始

### 步骤 1：列出可用串口

```
mcp__serial-port__list_ports
```

### 步骤 2：打开目标串口

```
mcp__serial-port__open_port --port "COM55" --baudrate 115200 --timeout 2.0
```

### 步骤 3：交互

```
# 发送命令（注意换行符 \n）
mcp__serial-port__write_data --data "cd /apps/helloworld\n"

# 读取返回
mcp__serial-port__read_data

# 发送下一个命令
mcp__serial-port__write_data --data "./helloworld\n"
mcp__serial-port__read_data
```

### 步骤 4：关闭

```
mcp__serial-port__close_port
```

## 常用波特率

| 设备类型 | 常用波特率 |
|----------|-----------|
| SylixOS | 115200 |
| Linux 嵌入式 | 115200, 57600, 9600 |
| AT 模块 | 115200, 9600 |
| 蓝牙串口 | 9600, 115200 |

## 注意事项

1. **换行符**：串口命令通常需要 `\n` 或 `\r\n` 结尾设备才会执行
2. **超时设置**：如果设备响应慢，增加 `timeout` 参数
3. **端口占用**：确保端口未被其他程序占用
4. **读写间隔**：发送命令后等待 0.3-1 秒再读取

## 工具完整列表

- `list_ports` - 列出所有可用串口
- `open_port` - 打开串口连接
- `close_port` - 关闭串口连接
- `read_data` - 从串口读取数据
- `write_data` - 向串口写入数据
- `get_status` - 获取当前连接状态
