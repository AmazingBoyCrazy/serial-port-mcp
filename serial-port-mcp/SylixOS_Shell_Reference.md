# SylixOS Shell 命令参考

SylixOS 是一个大型实时操作系统，不同于 Linux，有自己独特的 shell 命令体系。

## SylixOS vs Linux 主要区别

| 特性 | SylixOS | Linux |
|------|---------|-------|
| 标准目录 | `/apps`, `/bin`, `/etc`, `/root` | `/bin`, `/usr`, `/proc`, `/sys` |
| 模块加载 | `insmod`/`lsmod`/`rmmod` | `insmod`/`lsmod`/`rmmod` (相同) |
| 网络配置 | `ifconfig` | `ip addr` |
| 进程查看 | `ps` | `ps` (类似) |
| 系统信息 | `top`, `cpuus` | `top`, `uptime` |
| 关机 | `shutdown` | `shutdown`, `poweroff` |

## 常用命令速查

### 文件/目录操作

| 命令 | 功能 | 示例 |
|------|------|------|
| `ls` | 列出目录文件 | `ls`, `ls /apps` |
| `ll` | 详细列表 | `ll -l /apps` |
| `cd` | 切换目录 | `cd /apps/helloworld` |
| `pwd` | 显示当前目录 | `pwd` |
| `mkdir` | 创建目录 | `mkdir /apps/test` |
| `rmdir` | 删除目录 | `rmdir /apps/test` |
| `cat` | 显示文件内容 | `cat /etc/rc.conf` |
| `cp` | 复制文件 | `cp /bin/app /apps/` |
| `mv` | 移动/重命名 | `mv /apps/old /apps/new` |
| `rm` | 删除文件 | `rm /apps/test/file` |

### 进程/线程管理

| 命令 | 功能 | 示例 |
|------|------|------|
| `ps` | 查看进程 | `ps` |
| `top` | CPU 使用率 | `top` |
| `kill` | 发送信号 | `kill <pid>`, `kill -9 <pid>` |
| `killall` | 按名杀进程 | `killall appname` |
| `sleep` | 线程睡眠 | `sleep 5` (5秒) |
| `restart` | 重启进程 | `restart <pid>` |

### 网络命令

| 命令 | 功能 | 示例 |
|------|------|------|
| `ifconfig` | 网卡配置 | `ifconfig`, `ifconfig eth0` |
| `ifup` | 启用网卡 | `ifup eth0` |
| `ifdown` | 禁用网卡 | `ifdown eth0` |
| `ping` | 网络测试 | `ping 192.168.1.1` |
| `netstat` | 网络状态 | `netstat -a` |
| `arp` | ARP 表 | `arp -a` |

### 内存/存储

| 命令 | 功能 | 示例 |
|------|------|------|
| `free` | 内存信息 | `free` |
| `mems` | 内存详情 | `mems` |
| `df` | 文件系统 | `df -h` |
| `mount` | 挂载 | `mount -t devfs /dev/` |

### 模块加载 (动态加载)

| 命令 | 功能 | 示例 |
|------|------|------|
| `insmod` | 加载模块 | `insmod /lib/drivers/drv.ko` |
| `lsmod` | 查看模块 | `lsmod` |
| `rmmod` | 卸载模块 | `rmmod drv` |

### 系统命令

| 命令 | 功能 | 示例 |
|------|------|------|
| `reboot` | 重启 | `reboot` |
| `shutdown` | 关机 | `shutdown` |
| `date` | 日期时间 | `date`, `date -s "2024-01-01 12:00:00"` |
| `help` | 帮助 | `help`, `help <command>` |
| `ver` | 系统版本 | `ver` |

### 调试命令

| 命令 | 功能 | 示例 |
|------|------|------|
| `devs` | 设备列表 | `devs` |
| `drvs` | 驱动列表 | `drvs` |
| `ints` | 中断信息 | `ints` |
| `cpuus` | CPU 使用 | `cpuus` |

### 特殊命令

| 命令 | 功能 | 示例 |
|------|------|------|
| `vars` | 环境变量 | `vars` |
| `env` | 查看环境 | `env` |
| `echo` | 输出 | `echo $PATH` |
| `clear` | 清屏 | `clear` |
| `exit` | 退出登录 | `exit` |

## 常用工作流示例

### 1. 进入目录执行程序
```
cd /apps/helloworld
./helloworld
```

### 2. 查看系统资源
```
free          # 内存
df -h         # 磁盘
cpuus         # CPU
top           # 实时监控
```

### 3. 网络测试
```
ifconfig      # 查看 IP
ping 192.168.1.1
netstat -a     # 查看连接
```

### 4. 进程管理
```
ps            # 查看进程
kill <pid>    # 杀进程
restart <pid> # 重启
```

### 5. 模块操作
```
lsmod         # 已加载模块
insmod xxx.ko # 加载驱动
rmmod xxx     # 卸载驱动
```

### 6. 文件操作
```
cat /etc/rc.conf    # 查看配置
ls -l /apps/        # 列出文件
cp a.c /apps/       # 复制
rm /apps/a.c        # 删除
```

## 与 Linux 命令对比

### 相同点
- `ls`, `cd`, `pwd`, `cp`, `mv`, `rm`, `cat`, `mkdir` 基本相同
- `ping`, `kill`, `sleep` 相同
- `ifconfig` 参数相似

### 差异点
| Linux | SylixOS |
|-------|---------|
| `ip addr` | `ifconfig` |
| `pkill` | `killall` |
| `lsblk` | `df` |
| 无 | `cpuus` (CPU统计) |
| `lsmod` | 相同 |
| ` systemctl` | `reboot`/`shutdown` |

## 注意事项

1. **换行符**：串口命令需要 `\n` 结尾
2. **路径分隔符**：使用 `/`（与 Linux 相同）
3. **大小写敏感**：与 Linux 相同
4. **通配符**：`*`, `?` 支持
5. **Tab 补全**：支持命令补全

## 获取帮助

```
help                 # 所有命令
help <command>       # 特定命令
<command> --help     # 部分命令支持
```
