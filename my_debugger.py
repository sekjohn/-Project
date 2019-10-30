from ctypes import *
from my_debugger_defines import * 

kernel32 = windll.kernel32

class debugger():
    def __init__(self):
        pass
    def load(self,path_to_exe):
        #dwCreation 플래그를 이용해 프로세스를 어떻게 생성할 것인지 판단한다 
        #