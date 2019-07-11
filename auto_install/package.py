# coding=utf-8
from package_dsl  import *
from settings  import Settings
from package_global import Global

class Package:
        
    prefix_path = " "
	
    def __init__(self):
        self.filename = None

    def prefix(self, name):
        #设置安装目录
        self.filename = name
        setting = Settings()
        #print(setting.install_root())
        #print(setting.install_root()+"/"+setting.compiler_sets()+"/"+get_spec().version[0])
        self.prefix_path = setting.install_root() + "/" + self.filename + "-" + setting.compiler_sets()
        return self.prefix_path

# if __name__ == "__main__":
#    spec = None
#    a = Package()
#    print(a.prefix("s"))

