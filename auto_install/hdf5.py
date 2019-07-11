# coding=utf-8
import sys
sys.path.append('/home/xun/auto_install')
from package import Package
from package_dsl import *


class Hdf5(Package):
    global filename
    filename = "hdf5-1.10.5.tar.gz"
    path(filename)

    def install(self):
        #url("https://support.hdfgroup.org/ftp/HDF5/releases/hdf5-1.10/hdf5-1.10.5/src/hdf5-1.10.5.tar.gz")
        hash(filename, "6d4ce8bf902a97b050f6f491f4268634e252a63dadd6656a1a9be5b7b7726fa8")
        depends_on("zlib")
        depends_on("szip")

        args = " --enable-build-mode=production " \
               " --disable-dependency-tracking " \
               " --with-zlib=" + self.prefix("zlib-1.2.11") + \
               " --with-szlib=" + self.prefix("szip-2.1.1") + \
               " --enable-static=yes" \
               " --enable-shared=yes" \
               " --enable-fortran"

        configure("hdf5-1.10.5", self.prefix("hdf5-1.10.5") + args)
        make(" ")
        make("check")
        make("install")

if __name__ == "__main__":
    hdf5 = Hdf5()
    hdf5.install()