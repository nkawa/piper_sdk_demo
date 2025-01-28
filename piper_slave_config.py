#!/usr/bin/env python3
# -*-coding:utf8-*-
# 注意demo无法直接运行，需要pip安装sdk后才能运行
# 设置机械臂为从动臂
# 注意，如果是在机械臂处于主动臂模式下，发送设置指令后需要重新启动机械臂
#
# Note: The demo cannot run directly; the SDK must be installed via pip beforehand.
# Set the robotic arm to follower mode.
# Note: If the robotic arm is in active mode, you need to restart the robotic arm after sending the setting command.

from typing import (
    Optional,
)
import time
from piper_sdk import *

# 测试代码
# Test Code
if __name__ == "__main__":
    piper = C_PiperInterface()
    piper.ConnectPort()
    piper.MasterSlaveConfig(0xFC, 0, 0, 0)
