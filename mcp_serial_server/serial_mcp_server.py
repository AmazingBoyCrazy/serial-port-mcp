"""
MCP Serial Port Server
通过 MCP 协议提供串口通信能力
"""

import serial
import serial.tools.list_ports
from typing import Optional
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent
import asyncio

# 创建 MCP Server
server = Server("serial-port-server")

# 当前打开的串口连接
_active_connection: Optional[serial.Serial] = None


def list_serial_ports() -> list[dict]:
    """列出所有可用的串口"""
    ports = serial.tools.list_ports.comports()
    return [
        {
            "name": port.name,
            "device": port.device,
            "description": port.description,
            "hwid": port.hwid,
        }
        for port in ports
    ]


def open_serial_port(
    port: str,
    baudrate: int = 115200,
    bytesize: int = 8,
    parity: str = "N",
    stopbits: float = 1,
    timeout: Optional[float] = 1.0,
) -> dict:
    """打开串口连接"""
    global _active_connection

    if _active_connection and _active_connection.is_open:
        _active_connection.close()

    try:
        _active_connection = serial.Serial(
            port=port,
            baudrate=baudrate,
            bytesize=bytesize,
            parity=parity,
            stopbits=stopbits,
            timeout=timeout,
        )
        return {"success": True, "port": port, "message": f"已打开串口 {port}"}
    except Exception as e:
        return {"success": False, "error": str(e)}


def close_serial_port() -> dict:
    """关闭当前串口连接"""
    global _active_connection

    if _active_connection and _active_connection.is_open:
        _active_connection.close()
        _active_connection = None
        return {"success": True, "message": "串口已关闭"}
    return {"success": True, "message": "串口未打开"}


def read_from_serial(size: int = 1024) -> dict:
    """从串口读取数据"""
    global _active_connection

    if not _active_connection or not _active_connection.is_open:
        return {"success": False, "error": "串口未打开"}

    try:
        if _active_connection.in_waiting > 0:
            data = _active_connection.read(size)
            hex_data = data.hex() if data else ""
            return {
                "success": True,
                "data": data.decode("utf-8", errors="replace") if data else "",
                "hex": hex_data,
                "bytes_read": len(data),
            }
        return {"success": True, "data": "", "hex": "", "bytes_read": 0}
    except Exception as e:
        return {"success": False, "error": str(e)}


def write_to_serial(data: str, encoding: str = "utf-8") -> dict:
    """向串口写入数据"""
    global _active_connection

    if not _active_connection or not _active_connection.is_open:
        return {"success": False, "error": "串口未打开"}

    try:
        bytes_data = data.encode(encoding)
        written = _active_connection.write(bytes_data)
        _active_connection.flush()
        return {
            "success": True,
            "message": f"已写入 {written} 字节",
            "bytes_written": written,
        }
    except Exception as e:
        return {"success": False, "error": str(e)}


def get_connection_status() -> dict:
    """获取当前连接状态"""
    global _active_connection

    if _active_connection and _active_connection.is_open:
        return {
            "connected": True,
            "port": _active_connection.port,
            "baudrate": _active_connection.baudrate,
            "bytesize": _active_connection.bytesize,
            "parity": _active_connection.parity,
            "stopbits": _active_connection.stopbits,
            "timeout": _active_connection.timeout,
            "in_waiting": _active_connection.in_waiting,
        }
    return {"connected": False}


# 注册 MCP 工具
@server.list_tools()
async def list_tools() -> list[Tool]:
    return [
        Tool(
            name="list_ports",
            description="列出所有可用的串口设备",
            inputSchema={
                "type": "object",
                "properties": {},
            },
        ),
        Tool(
            name="open_port",
            description="打开指定的串口",
            inputSchema={
                "type": "object",
                "properties": {
                    "port": {"type": "string", "description": "串口名称，如 COM1"},
                    "baudrate": {
                        "type": "integer",
                        "description": "波特率，默认 115200",
                        "default": 115200,
                    },
                    "timeout": {
                        "type": "number",
                        "description": "超时时间（秒），默认 1.0",
                        "default": 1.0,
                    },
                },
                "required": ["port"],
            },
        ),
        Tool(
            name="close_port",
            description="关闭当前打开的串口",
            inputSchema={
                "type": "object",
                "properties": {},
            },
        ),
        Tool(
            name="read_data",
            description="从串口读取数据",
            inputSchema={
                "type": "object",
                "properties": {
                    "size": {
                        "type": "integer",
                        "description": "读取字节数，默认 1024",
                        "default": 1024,
                    },
                },
            },
        ),
        Tool(
            name="write_data",
            description="向串口写入数据",
            inputSchema={
                "type": "object",
                "properties": {
                    "data": {"type": "string", "description": "要发送的字符串数据"},
                    "encoding": {
                        "type": "string",
                        "description": "编码格式，默认 utf-8",
                        "default": "utf-8",
                    },
                },
                "required": ["data"],
            },
        ),
        Tool(
            name="get_status",
            description="获取当前串口连接状态",
            inputSchema={
                "type": "object",
                "properties": {},
            },
        ),
    ]


@server.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    """处理工具调用"""
    result: dict

    if name == "list_ports":
        ports = list_serial_ports()
        result = {"ports": ports, "count": len(ports)}

    elif name == "open_port":
        result = open_serial_port(
            port=arguments.get("port"),
            baudrate=arguments.get("baudrate", 115200),
            timeout=arguments.get("timeout", 1.0),
        )

    elif name == "close_port":
        result = close_serial_port()

    elif name == "read_data":
        result = read_from_serial(size=arguments.get("size", 1024))

    elif name == "write_data":
        result = write_to_serial(
            data=arguments.get("data"),
            encoding=arguments.get("encoding", "utf-8"),
        )

    elif name == "get_status":
        result = get_connection_status()

    else:
        result = {"error": f"未知工具: {name}"}

    return [TextContent(type="text", text=str(result))]


async def main():
    """主函数"""
    async with stdio_server() as (read_stream, write_stream):
        await server.run(read_stream, write_stream, server.create_initialization_options())


if __name__ == "__main__":
    asyncio.run(main())
