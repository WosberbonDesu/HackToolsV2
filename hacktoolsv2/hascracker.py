import hashlib
banner = """
  ___ ___    _____    _________ ___ ___  ___________________ ____  __.
 /   |   \  /  _  \  /   _____//   |   \ \_   ___ \______   \    |/ _|
/    ~    \/  /_\  \ \_____  \/    ~    \/    \  \/|       _/      <  
\    Y    /    |    \/        \    Y    /\     \___|    |   \    |  \ 
 \___|_  /\____|__  /_______  /\___|_  /  \______  /____|_  /____|__ \
       \/         \/        \/       \/          \/       \/        \/
WELCOME TO HASHCRACKER
"""
flag = 0
count = 0
print(banner)
 
pass_hash = input("Enter here md5 hash: ")


wordlist = input("Enter file name exp(password.txt): ")

try:

    pass_file = open(wordlist,"r")

except:

    print("No file found")
    print("Please check your file name and try again")
    quit()


for word in pass_file:

    encrypt_word = word.encode('utf-8')
    dige = hashlib.md5(encrypt_word.strip()).hexdigest()
    count += 1

    if dige == pass_hash:
        
        print("Password is found")
        print("After "+count+" try later")
        print("password is "+word)
        flag = 1
        break

if flag == 0:

    print("Password doens't found is not in list")


