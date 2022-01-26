from infi.systray import SysTrayIcon    #pip install infi.systray
from win32api import GetKeyState, GetAsyncKeyState
from win32con import VK_LSHIFT, VK_RSHIFT, VK_CAPITAL
import time

def majdetector(systray):
    print("Hello, World!")

menu_options = (("Detecteur de Maj", None, majdetector),)
systray = SysTrayIcon("vert.ico", "Detecteur de maj", menu_options)
systray.start()
    
while True:
    if GetKeyState(VK_CAPITAL):
        systray.update(icon="rouge.ico")
    else:
        if GetAsyncKeyState(VK_LSHIFT) == -32767:
            systray.update(icon="rouge.ico")
            time.sleep(0.5)
        else:
            if GetAsyncKeyState(VK_RSHIFT) == -32767:
                    systray.update(icon="rouge.ico")
                    time.sleep(0.5)
            else:
                systray.update(icon="vert.ico")
