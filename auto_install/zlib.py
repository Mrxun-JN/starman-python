# coding=utf-8
import sys
sys.path.append('/home/xun/auto_install')
from package import Package
from package_dsl import *

'''
每个软件包都有这样一个类，该类会设置软件包的一些基本信息，以及定义编译方法
'''
class Zlib(Package):
    global filename
    filename = "zlib-1.2.11.tar.gz"
    path(filename)

    def install(self):
        #url("https://zlib.net/zlib-1.2.11.tar.gz")
        hash(filename, "c3e5e9fdd5004dcb542feda5ee4f0ff0744628baf8ed2dd5d66f8ca1197cb1a1")

        configure("zlib-1.2.11", self.prefix("zlib-1.2.11"))
        make(" ")
        make("install")

if __name__ == "__main__":
    
    zlib = Zlib()
    zlib.install()