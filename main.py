import os
import sys
import subprocess
import time
import platform

print("are u ready motherfucker")
print("press any key to continue")
input()
time.sleep(2)
print("ok lets go")

script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "davirus.py")

if platform.system() == "Windows":
    subprocess.Popen([sys.executable, script_path], creationflags=subprocess.CREATE_NEW_CONSOLE)
else:
    # Linux/Mac - try common terminal emulators
    terminals = [
        ["gnome-terminal", "--", sys.executable, script_path],
        ["konsole", "-e", sys.executable, script_path],
        ["kitty", "-e", sys.executable, script_path],
        ["xfce4-terminal", "-e", f"{sys.executable} {script_path}"],
        ["xterm", "-e", sys.executable, script_path],
        ["open", "-a", "Terminal", script_path]  # macOS
    ]
    
    for cmd in terminals:
        try:
            subprocess.Popen(cmd)
            break
        except FileNotFoundError:
            continue
    else:
        # Fallback: run in same process if no terminal found
        subprocess.Popen([sys.executable, script_path])