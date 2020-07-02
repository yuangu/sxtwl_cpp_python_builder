#-*-coding:utf-8-*-
#build for sxtwl 1.0.7
import os
import sys
import platform
# import smtplib
from utils import Utils
# if sys.version_info < (3, 0):
#     from email import MIMEMultipart
#     from email import MIMEText
#     from email import MIMEBase
#     from email import Encoders 
#     from email.Utils import formatdate
# else:
#     import email.mime.text as  MIMEText
#     import email.mime.multipart as MIMEMultipart
#     import email.mime.base as MIMEBase
#     import email.encoders as Encoders
#     from email.utils import formatdate

#获取python文件所在的路径
def p():
    frozen = "not"
    if getattr(sys, 'frozen',False):
        frozen = "ever so"
        return os.path.dirname(sys.executable)

    return os.path.split(os.path.realpath(__file__))[0]

pyPath = p()

#更改工具目录
os.chdir(p())
#拉取代码
os.system("git clone https://github.com/yuangu/sxtwl_cpp.git")

#代码完成拉取
os.chdir(os.path.join(pyPath, "./sxtwl_cpp/python"))

print("=================开始执行python setup.py ========")
if platform.system() == 'Windows':
    print("打包执行中")
    PythonList = (
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
    )


    for python in PythonList:
        os.system( python + "  --version")
        os.system( python + "  -m pip install --upgrade pip")
        os.system( python + "  -m pip install --upgrade setuptools")
        os.system( python + "  -m pip  install wheel")
        os.system( python + "  setup.py bdist_wheel")
    #print(os.system("python setup.py  bdist_wininst"))
print("=================打包完成========")


#更换到打包好的目录里
# os.chdir(os.path.join(pyPath, "./sxtwl_cpp/python/dist"))

file_name = "dist.zip"
Utils.makeZipFile(file_name, os.path.join(pyPath, "./sxtwl_cpp/python/dist"))
print("打包zip包完成")




# #帐号和密码来源https://github.com/normal-four/test/blob/815393a266142ba64df0402f9a6c15c203b95156/spider/mailtest.py

# username = "wzp_test@126.com"
# passwd = "a1269325139"


# server = smtplib.SMTP('smtp.126.com')
# server.login(username,passwd)
# main_msg = MIMEMultipart.MIMEMultipart()


# from ffsend import upload
# url, owner =  upload("https://send.firefox.com/", file_name)
# file_name = None
# msg = u"这是一封自动发送的邮件，请不回复!\n您的打包结果下载地址:%s" %(url,)


# # 构造MIMEText对象做为邮件显示内容并附加到根容器
# text_msg = MIMEText.MIMEText(msg,'plain', "utf-8")
# main_msg.attach(text_msg)
 
# # 构造MIMEBase对象做为文件附件内容并附加到根容器
# contype = 'application/octet-stream'
# maintype, subtype = contype.split('/', 1)
 
# ## 读入文件内容并格式化
# # data = open(file_name, 'rb')
# # file_msg = MIMEBase.MIMEBase(maintype, subtype)
# # file_msg.set_payload(data.read( ))
# # data.close( )
# # Encoders.encode_base64(file_msg)
 
# # ## 设置附件头
# # basename = os.path.basename(file_name)
# # file_msg.add_header('Content-Disposition',
# #  'attachment', filename = basename)
# # main_msg.attach(file_msg)
 
# # 设置根容器属性
# main_msg['From'] = username
# main_msg['To'] = "1143402671@qq.com"
# # main_msg['Subject'] = "[sxtwl]打包结果通知"
# main_msg['Date'] = formatdate( )
 
# #带上python版本的信息
# # ext = ""
# # if "PYTHON_VERSION" in  os.environ:
# #     ext += "Python_" + os.environ['PYTHON_VERSION']

# # if "PYTHON_ARCH" in  os.environ:
# #     ext += "_" + os.environ['PYTHON_ARCH']

# main_msg['Subject'] = "[sxtwl]打包结果通知" 

# # 得到格式化后的完整文本
# fullText = main_msg.as_string( )
 
# # 用smtp发送邮件
# try:
#     server.sendmail(main_msg['From'], main_msg['To'], fullText)
# finally:
#     server.quit()
