from infi.systray import SysTrayIcon
from pynput import keyboard

def majdetector(systray):
    print("Hello, World!")

menu_options = (("Detecteur de Maj", None, majdetector),)
systray = SysTrayIcon("vert.ico", "Detecteur de maj", menu_options)
systray.start()


MAJ = False

def on_press(key):
    global MAJ
    try:
        if key == keyboard.Key.caps_lock:
            if MAJ:
                MAJ = False
            else:
                MAJ = True           

        elif key != key.caps_lock:
            print("another things")
    except AttributeError:
        print("AttributeError")
    
    if MAJ:
        systray.update(icon="rouge.ico")
    elif MAJ == False:
        systray.update(icon="vert.ico")



with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
    
