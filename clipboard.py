import pyperclip
import keyboard
import time


while True:
    try:
        if keyboard.is_pressed('ctrl+c'):
            print ('detected copy')
            cp = pyperclip.paste()
            cp = cp.replace("\n", " ")
            print (cp)
            pyperclip.copy(cp)
            time.sleep(2)
        if keyboard.is_pressed('ctrl+v'):
            print (pyperclip.paste())
        if keyboard.is_pressed('shift+q'):
            break;
    except:
        pass
