import platform
import pyuac
import tkinter as tk

from modules.popn_controller import PopnMusicController
from modules.love_live_ac_controller import LoveLiveController
from modules.iidx_controller import IIDXController
from modules.i2dx.server.i2dx_windows import activate_i2dx

def run_popn_controller(root):
    root.destroy()
    PopnMusicController().run()

def run_love_live_controller(root):
    root.destroy()
    LoveLiveController().run()

def run_iidxcontroller(root):
    root.destroy()
    IIDXController().run()

def run_i2dxcontroller(root):
    root.destroy()
    activate_i2dx()

def main():
    root = tk.Tk()
    root.title("Select Controller")

    tk.Label(root, text="Choose a controller to run:").pack(pady=10)

    tk.Button(root, text="Pop'n Music Controller", command=lambda: run_popn_controller(root)).pack(pady=5)
    tk.Button(root, text="Love Live Controller", command=lambda: run_love_live_controller(root)).pack(pady=5)
    tk.Button(root, text="On-screen IIDX Controller", command=lambda: run_iidxcontroller(root)).pack(pady=5)
    tk.Button(root, text="Web IIDX Controller (i2DX)", command=lambda:run_i2dxcontroller(root)).pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    if platform.system() == "Windows":
        if not pyuac.isUserAdmin():
            print("Re-launching as admin!")
            pyuac.runAsAdmin()
        else:
            main()
    else:
        main()