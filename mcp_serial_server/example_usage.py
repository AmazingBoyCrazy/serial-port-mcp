"""
MCP Serial Port Server 使用示例
展示如何在 Python 代码中调用 MCP 服务器的串口功能
"""

import json
import subprocess
import sys


def call_mcp_tool(tool_name: str, arguments: dict = None):
    """
    通过 MCP 协议调用工具的示例
    实际使用时需要 MCP 客户端库
    """
    pass


def demo():
    """演示序列"""
    print("=" * 50)
    print("MCP Serial Port Server 使用演示")
    print("=" * 50)

    # 示例 1: 列出所有可用串口
    print("\n[1] 列出可用串口:")
    print("    list_ports()")

    # 示例 2: 打开串口
    print("\n[2] 打开串口:")
    print('    open_port(port="COM3", baudrate=115200)')

    # 示例 3: 写入数据
    print("\n[3] 写入数据:")
    print('    write_data(data="AT\\r\\n")')

    # 示例 4: 读取数据
    print("\n[4] 读取数据:")
    print("    read_data()")

    # 示例 5: 获取状态
    print("\n[5] 获取连接状态:")
    print("    get_status()")

    # 示例 6: 关闭串口
    print("\n[6] 关闭串口:")
    print("    close_port()")

    print("\n" + "=" * 50)
    print("实际使用时请通过 MCP 客户端调用")
    print("=" * 50)


if __name__ == "__main__":
    demo()
