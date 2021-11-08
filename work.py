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
    from sxtw_build.python import PythonBuild 
    build = PythonBuild()

    ## linux 需要在manylinux里构建 
    if platform.system() == "Linux" and os.getenv("INOS") != 'docker':
        build.cmd("mkdir ./sxtwl_cpp/python/out")
        build.cmd("mkdir ./sxtwl_cpp/python/out/dist")

        l = (
            '--env PLA=manylinux1_x86_64  quay.io/pypa/manylinux1_x86_64 /opt/python/cp36-cp36m/bin/python work.py',
            # '--env PLA=manylinux1_i686 -i quay.io/pypa/manylinux1_i686 /opt/python/cp36-cp36m/bin/python work.py',
            # '--env PLA=manylinux2010_x86_64 -i quay.io/pypa/manylinux2010_x86_64 /opt/python/cp36-cp36m/bin/python work.py',
            # '--env PLA=manylinux2010_i686 -i quay.io/pypa/manylinux2010_i686 /opt/python/cp36-cp36m/bin/python work.py',
        )

        for v in l:
            cmd = "docker run --env BUILDFOR=python --env INOS=docker -v $PWD:/work -w /work  %s" %(v,)
            build.cmd(cmd)

        # 不知道为啥docker里无法上传wheel包，可能是docker命令没有-t
        build.twinePython = "$HOME/venv3.6/bin/python"
        build.cmd("ls ./sxtwl_cpp")
        build.cmd("ls ./sxtwl_cpp/python")
        build.cd("./sxtwl_cpp/python/out")
        build.after_build()        
    else:
    
        build.run()
else:
    print("不支持的构建语言目标")


