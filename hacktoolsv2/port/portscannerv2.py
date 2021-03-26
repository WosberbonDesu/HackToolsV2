import socket
from IPy import  IP

baner = """
root&root--> whoami 
<sk2gsrå.ape>
__________________ _______________________________________     _____    _______    _______  _____________________ 
\______   \_____  \\______   \__    ___/   _____/\_   ___ \   /  _  \   \      \   \      \ \_   _____/\______   \
 |     ___//   |   \|       _/ |    |  \_____  \ /    \  \/  /  /_\  \  /   |   \  /   |   \ |    __)_  |       _/
 |    |   /    |    \    |   \ |    |  /        \\     \____/    |    \/    |    \/    |    \|        \ |    |   \
 |____|   \_______  /____|_  / |____| /_______  / \______  /\____|__  /\____|__  /\____|__  /_______  / |____|_  /
                  \/       \/                 \/         \/         \/         \/         \/        \/         \/

Welcome to port scanner
"""

print(baner)

class PortScan():   
    banners = []
    open_ports = []

    def __init__(self,target,port_num):
        self.target = target
        self.port_num = port_num
        

    def scan(self):
    
        #converted_ip = check_ıp(target)
        #print("\n"+"-_o Scanning target "+ str(target)+"<-^_^->")

        for port in range(1,500):

            self.scanner_port(port)

    def check_ıp(self):

        try:

            IP(self.target)
            return(self.target)

        except ValueError:
       
            return socket.gethostname(self.target) 

    #def get_banner(self):

        #return soc.recv(1024)


    def scanner_port(self,port):

        try:
            converted_ip = self.check_ıp()

            sock = socket.socket()
            sock.settimeout(0.5)
            sock.connect((converted_ip,port))

            self.open_ports.append(port)
            try: 
                banner = sock.recv(1024).decode().strip('\n').strip("\r")# self.get_banner(sock)
                #print("[+] Port"+ str(port)+ " is open" + " : "+ str(banner.decode().strip("\n")))
                self.banners.append(banner)

            except:
                # print("[+] Port"+ " is open : "+ str(port))
                self.banners.append(" ")
            sock.close()

        except:
            pass

        # print("[+] Port "+ str(port)+ " is closed")

    #informations = """
    #1. You can write like this www.google.com
    #2. You can write like this https.www.google.com.ru 
    #3. You can write like this 192.12.1.1
    #4. You can write like this google.com
    #5. google.com,spacex.com,nasa.org you can simply split with this , and easily check them 
    #All of them is okay just be carefull while you writing 
    #Good Luck, Have Fun.
    #"""

    #print(informations)
    #if __name__ == "__main__":
    
        #targets = input("[+] Enter target name/s to scan: (split multiple targets with -> ',') ")
        #portnum = input("Enter number of ports that you want to scan: ")

        #if "," in targets:
        
            #for ip_add in targets.split(","):

                #scan(ip_add.strip(" "),portnum)
        #else:
            #scan(targets,portnum)

    # converted_ip = check_ıp(ipaddress)
    # print("Target ip adress: "+converted_ip)

    #for port in range(75,85):
    
    #scanner_port(converted_ip,port)