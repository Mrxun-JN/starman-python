# coding=utf-8
import sys
import os.path
import re
'''
PackageSpec 类定义一个规范，这个规范包含下载地址、本地地址、文件名、版本号、依赖等基本信息
PackageSpec 类同时还定义了以下设置上述规范信息的方法
'''
class PackageSpec:
    def __init__(self):
        self.url = None  #软件下载地址
        self.path = None #软件本地路径
        self.sha256 = None
        self.version = None
        self.file_name = None

    def set_hash(self,val):
        self.sha256 = val

    def set_url(self,val):
        # 解析路径，下载
        self.url = val
        os.system("wget -P /home/xun/auto_install/test/download " + self.url)

    def set_path(self,val):
        #截取路径中的文件名，版本号
        self.path = val
        self.file_name = os.path.basename(val)
        self.version = re.findall(r"(\d+\.\d+(\.\d+(\.\d+)?)?)",self.file_name)
        self.version = self.version[0][0]
        #self.version = re.findall(r".*-(\d +\.\d + (\.\d + (\.\d +)?)?)",self.file_name)
        print("print from package_spec")
        print(self.version)
        print(self.file_name)
  
# a = PackageSpec()
# a.set_path("/home/weyzhang/Work/project/auto-install/python-test/zlib-1.0.tar.gz")
