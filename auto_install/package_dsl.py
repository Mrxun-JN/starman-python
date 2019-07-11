# coding=utf-8
import sys
sys.path.append('/home/xun/auto_install')
import os

from package_spec import PackageSpec
from package_global import Global

'''
软件编译过程常需要的方法函数
'''
def get_spec():
    if not Global.spec:
        Global.spec = PackageSpec()
    return Global.spec
# 下载、解压
def url(val):
    get_spec().set_url(val)

# 截取路径中的文件名，版本号
def path(val):
    get_spec().set_path(val)

# 检查文件完整性
def hash(app, val):
    import hashlib
    get_spec().set_hash(val)
    f = open("/home/xun/auto_install/test/download/" + app, 'rb')
    sha = hashlib.sha256()
    sha.update(f.read())
    if sha.hexdigest() == val:
        print("sha256 has been checked completely!")
    else:
        print("File is not completed!")
        exit(0)

def run(val):
    #python执行shell命令
     os.system(val)

def make(val):
    # 调用run执行make 或者 make install
    run("make " + val)

def configure(filename, val):
    # 调用 run 执行 configure
    os.chdir("/home/xun/auto_install/test/download")
    run("tar -zxvf " + filename + ".tar.gz")
    os.chdir("/home/xun/auto_install/test/download/" + filename)
    run("./configure --prefix=" + val)

def depends_on(app):
    # 软件依赖
    import fnmatch

    where_search = "/home/xun/auto_install/test/temp"
    filenames = os.listdir(where_search)
    result = len(filenames)
    num = 0

    for filename in filenames:
        if fnmatch.fnmatch(filename, app + "*") == False:
            num += 1

    if num == result:
        run("python3 " + app + ".py")
    else:
        print("Dependence has been installed!")



# if __name__ == "__main__":
#     depends_on("zlb")

# hash("zlib-1.2.11.tar.gz", "c3e5e9fdd5004dcb542feda5ee4f0ff0744628baf8ed2dd5d66f8ca1197cb1a1")