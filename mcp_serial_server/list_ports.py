#!/usr/bin/env python3
"""列出所有可用的串口"""

try:
    import serial.tools.list_ports
    ports = serial.tools.list_ports.comports()
    print(f"找到 {len(ports)} 个串口设备:\n")
    for i, port in enumerate(ports, 1):
        print(f"  {i}. {port.device}")
        print(f"     名称: {port.name}")
        print(f"     描述: {port.description}")
        print(f"     硬件ID: {port.hwid}")
        print()
except ImportError:
    print("错误: 需要安装 pyserial")
    print("运行: pip install pyserial")
