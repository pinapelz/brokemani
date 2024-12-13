import platform

import pyuac

from modules.popn_controller import PopnMusicController


def main():
    PopnMusicController().run()

if __name__ == "__main__":
    if platform.system() == "Windows":
        if not pyuac.isUserAdmin():
            print("Re-launching as admin!")
            pyuac.runAsAdmin()
        else:
            main()
    else:
        main()
