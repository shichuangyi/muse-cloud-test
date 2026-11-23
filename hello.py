import platform
from datetime import datetime

print("你好，这是 GitHub 云端运行的代码")
print(f"操作系统：{platform.system()} {platform.release()} ({platform.machine()})")
print(f"Python 版本：{platform.python_version()}")
print(f"当前时间：{datetime.now().astimezone().isoformat(sep=' ', timespec='seconds')}")
