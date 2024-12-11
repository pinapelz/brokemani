from modules.popn_controller import PopnMusicController

import pyuac

def main():
    PopnMusicController().run()

if __name__ == "__main__":
    if not pyuac.isUserAdmin():
        print("Re-launching as admin!")
        pyuac.runAsAdmin()
    else:        
        main()
