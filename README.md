# ROS-CarsControlDemo

## 本程序在wsl2中运行
驱动等具体安装步骤见 https://learn.microsoft.com/zh-cn/windows/wsl/connect-usb

将xbee设备挂载到wsl2中需要进行如下操作
1. 通过以管理员模式打开 PowerShell 并输入以下命令，列出所有连接到 Windows 的 USB 设备：
```PowerShell
usbipd wsl list
```

2. 选择要附加到 WSL 的设备总线 ID，然后运行此命令。 WSL 会提示你输入密码以运行 sudo 命令。 要附加的 Linux 分发版必须是默认分发版。 (请参阅 WSL 文档的基本 comands 以更改默认分发) 。
```PowerShell
usbipd wsl attach --busid <busid>
```

3. 打开 Ubuntu（或首选的 WSL 命令行），使用以下命令列出附加的 USB 设备：
```Bash
lsusb
```
你应会看到刚刚附加的设备，并且能够使用常规 Linux 工具与之交互。 根据你的应用程序，你可能需要配置 udev 规则以允许非根用户访问设备。

4. 在 WSL 中完成设备使用后，可物理断开 USB 设备，或者在管理员模式下从 PowerShell 运行此命令：
``` PowerShell
usbipd wsl detach --busid <busid>
```