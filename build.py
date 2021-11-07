import platform
import os
import sys

sys.path.append("./build")

## 如果是python构建任务，执行python构建任务
if os.getenv('BUILDFOR') == "python":
    from build import python
    python.PythonBuild().run()
else:
    print("不支持的构建语言目标")


