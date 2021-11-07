import platform
import os
import sys

def p():
    frozen = "not"
    if getattr(sys, 'frozen',False):
        frozen = "ever so"
        return os.path.dirname(sys.executable)

    return os.path.split(os.path.realpath(__file__))[0]

pyPath = p()


sys.path.append( os.path.join(pyPath,  "./build"))

## 如果是python构建任务，执行python构建任务
if os.getenv('BUILDFOR') == "python":
    from build import python
    python.PythonBuild().run()
else:
    print("不支持的构建语言目标")


