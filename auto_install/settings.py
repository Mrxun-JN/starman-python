# coding=utf-8
import yaml
import os

#读取配置文件 starman.yml，获得编译器、build路径、安装路径等信息
class Settings:
    #解压编译目录
    def cache_root(self):
        '/tmp/starman'
        pass
    #安装目录
    def install_root(self):
        return self.settings['install_root']
    #选择哪个系列编译器
    def compiler_sets(self):
        return self.settings['defaults']['compiler_set']
    def compilers(self):
        return self.settings['compiler_sets'][self.compiler_sets()]
    def c_compiler(self):
        return self.compilers()['c']
    def cxx_compiler(self):
        return self.compilers()['cxx']
    def fortran_compiler(self):
        return self.compilers()['fortran']

    def __init__(self):
        f = open(r'./starman.yml')
        self.settings  = yaml.load(f, Loader=yaml.FullLoader) # Loader is new request,detail in https://github.com/yaml/pyyaml/wiki/PyYAML-yaml.load(input)-Deprecation
        os.environ['CC'] = self.c_compiler()
        os.environ['CXX'] = self.cxx_compiler()
        os.environ['FC'] = self.fortran_compiler()
        os.environ['F77'] = self.fortran_compiler()

# a = Settings()
# print(a.install_root())
# print(a.compiler_sets())
# print(a.compilers())
# print(a.c_compiler())
# print(a.cxx_compiler())
# print(a.fortran_compiler())
# print(os.environ['CC'])
# print(os.environ['CXX'])
# print(os.environ['FC'])
# print(os.environ['F77'])
