import os

pythonList = os.listdir("/opt/python/")
print(pythonList)
for d in pythonList:
    pythonPath = os.path.join('/opt/python/', d)
    pythonPath = os.path.join(pythonPath, 'bin/python')
    if d.find("cp") < 0:
        pass
    else:
        print(pythonPath)