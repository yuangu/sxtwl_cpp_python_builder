import os

class BuildBase:
    workDir = ""

    def cmd(self, cmd):
        os.system(cmd)

    def before_build(self):
        pass

    def build(self):
        pass

    def after_build(self):
        pass
    

    def run(self):
        self.workDir = os.getcwd()
        print("before_build")
        self.before_build()

        print("build")
        self.build()

        print("after_build")
        self.after_build()