# coding=utf-8
import sys
sys.path.append('/home/xun/auto_install')
from package import Package
from package_dsl import *


class Szip(Package):
    global filename
    filename = "szip-2.1.1.tar.gz"
    path(filename)

    def install(self):
        #url("https://support.hdfgroup.org/ftp/lib-external/szip/2.1.1/src/szip-2.1.1.tar.gz")
        hash(filename, "21ee958b4f2d4be2c9cabfa5e1a94877043609ce86fde5f286f105f7ff84d412")

        args = " --disable-debug " \
               " --disable-dependency-tracking"

        configure("szip-2.1.1", self.prefix("szip-2.1.1") + args)
        make(" ")
        make("install")

if __name__ == "__main__":
    szip = Szip()
    szip.install()