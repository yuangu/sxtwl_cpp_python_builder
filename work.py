import os
import sys
import platform

def p():
    frozen = "not"
    if getattr(sys, 'frozen',False):
        frozen = "ever so"
        return os.path.dirname(sys.executable)

    return os.path.split(os.path.realpath(__file__))[0]

pyPath = p()

sys.path.append(os.path.join(pyPath,  "./"))
sys.path.append( os.path.join(pyPath,  "./sxtw_build"))

## 如果是python构建任务，执行python构建任务
if os.getenv('BUILDFOR') == "python" :
    if platform.system() == "Linux" and os.getenv("INOS") != 'docker':
        cmd = "docker run --env BUILDFOR=python --env INOS=docker --env TWINE_PASS=$TWINE_PASS -DPUSH_PIP=$PUSH_PIP -v $PWD:/work -w /work -it quay.io/pypa/manylinux_2_24_x86_64 /opt/python/cp36-cp36m/bin/python work.py"
        os.system(cmd)
        exit()

    from sxtw_build.python import PythonBuild 
    # from build import python
    PythonBuild().run()
else:
    print("不支持的构建语言目标")


