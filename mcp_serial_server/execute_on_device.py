#!/usr/bin/env python3
"""
通过串口连接设备，执行命令并获取返回数据
"""

import serial
import time
import sys

# 串口配置
SERIAL_PORT = "COM55"
BAUDRATE = 115200
TIMEOUT = 2.0

# 执行命令
COMMANDS = [
    "cd /apps/helloword\n",
    "./helloworld\n",  # 注意：如果是 helloword 就改成 helloword
]

def execute_via_serial():
    """通过串口执行命令并获取返回"""
    try:
        print(f"[*] 连接串口 {SERIAL_PORT}...")
        ser = serial.Serial(
            port=SERIAL_PORT,
            baudrate=BAUDRATE,
            timeout=TIMEOUT,
            write_timeout=5.0
        )
        print(f"[+] 串口已打开\n")

        # 等待设备就绪
        time.sleep(0.5)
        ser.read_all()  # 清空缓冲区

        output = []

        for cmd in COMMANDS:
            print(f"[>] 发送: {repr(cmd)}")
            ser.write(cmd.encode('utf-8'))
            time.sleep(0.3)  # 等待命令执行

            # 读取返回数据
            response = b""
            start_time = time.time()
            while time.time() - start_time < TIMEOUT:
                if ser.in_waiting > 0:
                    response += ser.read(ser.in_waiting)
                    time.sleep(0.1)
                else:
                    break

            if response:
                decoded = response.decode('utf-8', errors='replace')
                print(f"[<] 返回:\n{decoded}\n")
                output.append(decoded)
            else:
                print(f"[<] 无返回数据\n")

        ser.close()
        print("[*] 串口已关闭")
        return "\n".join(output)

    except serial.SerialException as e:
        print(f"[!] 串口错误: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"[!] 错误: {e}")
        sys.exit(1)


if __name__ == "__main__":
    result = execute_via_serial()
    print("\n" + "=" * 50)
    print("最终返回结果:")
    print("=" * 50)
    print(result)
