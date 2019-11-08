from ctypes import *

WORD =  c_ushort
DWORD = c_ulong
LPBYTE = POINTER(c_ubyte)
LPTSTR = POINTER(c_char)
HANDLE = c_void_p

DEBUG_PROCESS = 0x00000001
CREATE_NEW_CONSOLE = 0x00000010

# CreateProcessA()함수
class STARTUPINFO(Structure):
    _fields_=[
        ("cb",DWORD),
        ("lqReserved",LPTSTR),
        ("lpDesktop",LPTSTR),
        ("lpTitle",LPTSTR),
        ("dwX",DWORD),
        ("dwY",DWORD),
        ("dwXSize",DWORD),
        ("dwYSize",DWORD),
        ("dwXCountChars",DWORD),
        ("dwYCountChars",DWORD),
        ("dwFillAttribute",DWORD),
        ("dwFlags",DWORD),
        ("wShowWindow",WORD),
        ("cbReserved2",WORD),
        ("lpReserved2",LPBYTE),
        ("hStdInput",HANDLE),
        ("hStdOutput",HANDLE),
        ("hStdError",HANDLE),
    ]
        
class PROCESS_INFORMAIION(Structure):
    _fields_ = [
        ("hProcess",HANDLE),
        ("hThread",HANDLE),
        ("dwProcessId",DWORD),
        ("dwThreadId",DWORD),
        ]



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
 
        if kernel32.CreateProcessW(path_to_exe,None,None,None,None,creation_flags,None,None,byref(startupinfo),byref(process_informaiion)):
            print("[*] We have successfully launched the process !")
            print("[*]PID : %d"%process_informaiion.dwProcessId)
        else :
            print("[*] Error: 0x%08x."%kernel32.GetLastError())

debugger12 = debugger()

debugger12.load("C:\Windows\System32\calc.exe") 