# MCP Serial Port Server

通过 Model Context Protocol (MCP) 提供串口通信能力的服务器。

## 安装

```bash
pip install -r requirements.txt
```

## 使用方法

### 启动服务器

```bash
python serial_mcp_server.py
```

### 可用工具

| 工具名 | 描述 | 参数 |
|--------|------|------|
| `list_ports` | 列出所有可用串口 | 无 |
| `open_port` | 打开串口 | `port` (必需), `baudrate` (默认 115200), `timeout` (默认 1.0) |
| `close_port` | 关闭串口 | 无 |
| `read_data` | 读取串口数据 | `size` (默认 1024) |
| `write_data` | 向串口写入数据 | `data` (必需), `encoding` (默认 utf-8) |
| `get_status` | 获取连接状态 | 无 |

### 使用示例

```python
# 1. 列出可用串口
list_ports()

# 2. 打开串口
open_port(port="COM3", baudrate=115200)

# 3. 写入数据
write_data(data="Hello Device")

# 4. 读取响应
read_data()

# 5. 关闭串口
close_port()
```

## 配置文件 (config.json)

```json
{
  "serial": {
    "default_baudrate": 115200,
    "default_timeout": 1.0,
    "default_bytesize": 8,
    "default_parity": "N",
    "default_stopbits": 1
  }
}
```

## 注意事项

- 确保串口未被其他程序占用
- 读取数据是非阻塞的，如果串口缓冲区没有数据会返回空
- 写入后建议适当延时再读取
- 某些设备可能需要特定的换行符（如 `\r\n` 或 `\n`）
