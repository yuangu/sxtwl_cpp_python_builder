import  base
import platform

class PythonBuild(base.BuildBase):
    pythonList = []

    def before_build(self):
        print("os:", platform.system())
        if platform.system() == 'Windows':
            # self.cmd('set PATH=%PYTHON%;%PYTHON%//scripts;%PATH%')
            self.cmd('set VS90COMNTOOLS=%VS140COMNTOOLS%')
            self.cmd('set VS100COMNTOOLS=%VS140COMNTOOLS%')
            self.cmd('echo %VS90COMNTOOLS%')

            self.cmd('cd "c:/Users/appveyor/AppData/Local/Programs/Common/Microsoft/"')
            self.cmd( 'ren "Visual C++ for Python" "Visual C++ for Python Do Not Use"')

            self.cmd( 'cd "C:/Program Files (x86)/"')
            self.cmd( 'ren "Microsoft Visual Studio 9.0" "Microsoft Visual Studio 9.0 Do Not Use"')
            self.cmd( 'ren "Microsoft Visual Studio 10.0" "Microsoft Visual Studio 10.0 Do Not Use"')

            # 回到工作目录
            self.cmd("cd " + self.workDir)

            self.pythonList = [
                "C:\\Python26\\python.exe",
                "C:\\Python26-x64\\python.exe",
                "C:\\Python27\\python.exe",
                "C:\\Python27-x64\\python.exe",
                "C:\\Python33\\python.exe",
                "C:\\Python33-x64\\python.exe",
                "C:\\Python34\\python.exe",
                "C:\\Python34-x64\\python.exe",
                "C:\\Python35\\python.exe",
                "C:\\Python35-x64\\python.exe",
                "C:\\Python36\\python.exe",
                "C:\\Python36-x64\\python.exe",
                "C:\\Python37\\python.exe",
                "C:\\Python37-x64\\python.exe",
                "C:\\Python38\\python.exe",
                "C:\\Python38-x64\\python.exe",
            ]

        # 拉取代码
        self.cmd("git clone https://github.com/yuangu/sxtwl_cpp.git")
        
        # 代码完成了
        self.cmd("cd ./sxtwl_cpp/python")


    def build(self):
        for python in self.pythonList:
            self.cmd( python + "  --version")
            self.cmd( python + "  -m pip install --upgrade pip")
            self.cmd( python + "  -m pip install --upgrade setuptools")
            self.cmd( python + "  -m pip  install wheel")
            self.cmd( python + "  setup.py bdist_wheel")