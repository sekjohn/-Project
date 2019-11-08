from ctypes import *
from my_debugger_defines import * 

kernel32 = windll.kernel32

class debugger():
    def __init__(self):
        pass
    def load(self,path_to_exe):
        
        creation_flags = DEBUG_PROCESS
        
        startupinfo = STARTUPINFO()
        process_informaiion = PROCESS_INFORMAIION()

        startupinfo.dwFlags = 0x1
        startupinfo.wShowWindow = 0x0

        startupinfo.cb = sizeof(startupinfo)
        #파이썬3.x 대부터 CreateProcessA가 아니라 utf-8E사용하기떄문에 CreateProcessW사용  
        if kernel32.CreateProcessW(path_to_exe,None,None,None,None,creation_flags,None,None,byref(startupinfo),byref(process_informaiion)):
            print("[*] We have successfully launched the process !")
            print("[*]PID : %d"%process_informaiion.dwProcessId)
        else :
            print("[*] Error: 0x%08x."%kernel32.GetLastError())
