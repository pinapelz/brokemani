import platform
import pyuac
import tkinter as tk

from modules.popn_controller import PopnMusicController
from modules.love_live_ac_controller import LoveLiveController

def run_popn_controller(root):
    root.destroy()
    PopnMusicController().run()

def run_love_live_controller(root):
    root.destroy()
    LoveLiveController().run()

def main():
    root = tk.Tk()
    root.title("Select Controller")

    tk.Label(root, text="Choose a controller to run:").pack(pady=10)

    tk.Button(root, text="Pop'n Music Controller", command=lambda: run_popn_controller(root)).pack(pady=5)
    tk.Button(root, text="Love Live Controller", command=lambda: run_love_live_controller(root)).pack(pady=5)

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