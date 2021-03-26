import hashlib
import sys 
import os
import base64
from tkinter import *
from tkinter import file

#message_bytes = message.encode('ascii')
#base64_bytes = base64.b64encode(message_bytes)
#base64_message = base64_bytes.decode('ascii')

#print(base64_message)

banner = """
sk2gsrå.ape
  ___ ___    _____    _________ ___ ___  ___________________    _____  _________  ____  __._____________________ 
 /   |   \  /  _  \  /   _____//   |   \ \_   ___ \______   \  /  _  \ \_   ___ \|    |/ _|\_   _____/\______   \
/    ~    \/  /_\  \ \_____  \/    ~    \/    \  \/|       _/ /  /_\  \/    \  \/|      <   |    __)_  |       _/
\    Y    /    |    \/        \    Y    /\     \___|    |   \/    |    \     \___|    |  \  |        \ |    |   \
 \___|_  /\____|__  /_______  /\___|_  /  \______  /____|_  /\____|__  /\______  /____|__ \/_______  / |____|_  /
       \/         \/        \/       \/          \/       \/         \/        \/        \/        \/         \/
"""

options = """
1.[+] md5
2.[+] sha1
3.[+] sha224
4.[+] sha384
5.[+] sha256
6.[+] sha512
7.[+] blake2b
8.[+] base64      
9.[+] shake_128
10.[+] img2
11.[+] img1jpg
12.[+] img1png
"""
print(banner)

type_of_hash = str(input("Which type of hash you want to bruteforce: "))
type_of_hash = type_of_hash.lower()
file_path = str(input("Enter file to bruteforce with: "))

hash_to_decrypt = str(input('Enter Hash Value to bruteforce: '))
print("For encryption you can choose= ")
print(options)
ques = str(input("Do you wanna encryption to string? (yes/no):  "))
ques = ques.lower()

if ques == 'yes':
    
    vi = str(input("Please choose encryption hash: (md5,sha1): "))
    vi = vi.lower()
    if vi == 'md5':

        glia = hashlib.md5()
        bellek = str(input("Enter the word to be translated: "))
        bellek = bellek.lower()
        bellek = bellek.strip().encode()
        glia.update(bellek)
        #glia.hexdigest()
        print("MD5 ENCRPTION")
        print("||||||||")
        print('↓↓↓↓↓↓↓↓')
        print(glia.hexdigest())
        print(glia.block_size)
    
    elif vi == 'sha1':
    
        glia = hashlib.sha1()
        bellek = str(input("Enter the word to be translated: "))
        bellek = bellek.lower()
        bellek = bellek.strip().encode()
        glia.update(bellek)
        #glia.hexdigest()
        print("SHA1 ENCRPTION")
        print("||||||||")
        print('↓↓↓↓↓↓↓↓')
        print(glia.hexdigest())
        print(glia.block_size)

    elif vi == 'sha224':
        
        glia = hashlib.sha224()
        bellek = str(input("Enter the word to be translated: "))
        bellek = bellek.lower()
        bellek = bellek.strip().encode()
        glia.update(bellek)
        #glia.hexdigest()
        print("sha224 ENCRPTION")
        print("||||||||")
        print('↓↓↓↓↓↓↓↓')
        print(glia.hexdigest())
        print(glia.block_size)

    elif vi == 'sha384':
        
        glia = hashlib.sha384()
        bellek = str(input("Enter the word to be translated: "))
        bellek = bellek.lower()
        bellek = bellek.strip().encode()
        glia.update(bellek)
        #glia.hexdigest()
        print("sha384 ENCRPTION")
        print("||||||||")
        print('↓↓↓↓↓↓↓↓')
        print(glia.hexdigest())
        print(glia.block_size)

    elif vi == 'sha256':
        
        glia = hashlib.sha256()
        bellek = str(input("Enter the word to be translated: "))
        bellek = bellek.lower()
        bellek = bellek.strip().encode()
        glia.update(bellek)
        #glia.hexdigest()
        print("sha256 ENCRPTION")
        print("||||||||")
        print('↓↓↓↓↓↓↓↓')
        print(glia.hexdigest())
        print(glia.block_size)

    

    elif vi == 'sha512':
        
        glia = hashlib.sha512()
        bellek = str(input("Enter the word to be translated: "))
        bellek = bellek.lower()
        bellek = bellek.strip().encode()
        glia.update(bellek)
        #glia.hexdigest()
        print("sha512 ENCRPTION")
        print("||||||||")
        print('↓↓↓↓↓↓↓↓')
        print(glia.hexdigest())
        print(glia.block_size) 


    elif vi == 'blake2b':
        
        glia = hashlib.blake2b()
        bellek = str(input("Enter the word to be translated: "))
        bellek = bellek.lower()
        bellek = bellek.strip().encode()
        glia.update(bellek)
        #glia.hexdigest()
        print("blake2b ENCRPTION")
        print("||||||||")
        print('↓↓↓↓↓↓↓↓')
        print(glia.hexdigest())
        print(glia.block_size)

    elif vi == 'base64':

        message = str(input("Enter the word to be translated: "))
        message_bytes = message.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode('ascii')

        print(base64_message)

    elif vi == 'shake_128':
        gfg = hashlib.shake_128()
        gfg.update(b'GeeksForGeeks')
        
        print(gfg.digest(10))

    elif vi == 'img1jpg':

        glia = str(input("Enter Image name exp(glia.jpg) :"))
        file = open(glia,'rb')
        image = file.read()
        file.close()
        image = bytearray(image)
        key = 48
        for i,j in enumerate(image):

            image[i] = j^key
        file = open("encrypted.jpg","wb")
        file.write(image)
        file.close()

    elif vi == 'img1png':
    
        glia = str(input("Enter Image name exp(glia.png) :"))
        file = open(glia,'rb')
        image = file.read()
        file.close()
        image = bytearray(image)
        key = 48
        for i,j in enumerate(image):

            image[i] = j^key
        file = open("encrypted.png","wb")
        file.write(image)
        file.close()

    elif vi == "img2":

        storingbasedata = ""

        file_folder_path = sys.argv[1]

        def read_image_path(imagepath):

            global storingbasedata
            with open(imagepath,"rb") as file:

                base64_image = base64.b64encode(file.read())
                appendData(base64_image)
                return storingbasedata

        def appendData(dataTobeAppended):

            global storingbasedata

            formatted_string = "{}".format(dataTobeAppended)
            formatted_string = formatted_string[2:1]
            storingbasedata += formatted_string

        def check_if_file_or_directory(locationPath):

            returnin_statement = False 
            if(os.path.isdir(locationPath)):
                returnin_statement = "Folder"
            elif(os.path.isfile(locationPath)):
                returnin_statement = "File"
            else:
                print("FORMAT IS EMPTY")
            return returnin_statement

        def process_folder(folderPath):

            supported_files = []
            supported_extensions = ["jpg","png","gif","jpeg"]

            for file in os.listdir(folderPath):
                for extension in supported_extensions:
                    if(file.endswith("."+extension)):
                        supported_files.append(file)
                        print("Found : ",file)
                    else:
                        print("The format you wrote is not supported or you have entered incorrectly.")
            return supported_files

        def save_data():

            global storingbasedata
            with open("encryptedfile.encrypteddoc","w+") as file:

                file.write(storingbasedata)
                file.close()
        
        while True:
            def lexie():

                global storingbasedata
                is_file_or_dir = check_if_file_or_directory(file_folder_path)

                if(is_file_or_dir == "Folder"):
                    iteration_count = 0
                    for eachFile in process_folder(file_folder_path):
                        if(not iteration_count == 0):
                            storingbasedata += "*"
                        read_image_path(file_folder_path+eachFile)
                        iteration_count += 1
                        save_data()

                    
                elif(is_file_or_dir == "File"):
                    read_image_path(file_folder_path)
                    save_data()
                else:
                    print("Invalid Path")
        
    elif vi == "cool":

        root = Tk()
        root.geometry("300x240")
        def encrypt_image():
            file1 = root.filedialog.askopenfilename(mode='r',filetype=[('jpg file','*.jpg')])
            if file1 is not None:
                print(file1)
                file_name = file1.name
                print(file_name)
                key = entry1.get(1.0,END)
                print(file_name,key)
                ve = open(file_name,'rb')
                image = ve.read()
                ve.close()
                image=bytearray(image)
                for index,values in enumerate(image):
                    image[index] = values^int(key)
                fi1 = open(file_name,'wb')
                fi1.write(image)
                fi1.close()
        b1 = Button(root,text = "encrypt",command=encrypt_image)
        b1.place(x=105,y=15)
        entry1 = Text(root,height=1,width=10)
        entry1.place(x=75,y=75)
        root.mainloop()



elif ques == 'no':

    with open(file_path,'r') as file:

        for line in file.readlines():

            if type_of_hash == 'md5':

                hash_object = hashlib.md5(line.strip().encode())

                hashed_word = hash_object.hexdigest()

                if hashed_word == hash_to_decrypt:

                    print("Found! MD5 PASSWORD")
                    print("PASSWORD")
                    print("||||||||")
                    print('↓↓↓↓↓↓↓↓')
                    print(line.strip())
                    exit(0)

            elif type_of_hash == 'sha1':

                hash_object = hashlib.sha1(line.strip().encode())

                hashed_word = hash_object.hexdigest()

                if hashed_word == hash_to_decrypt:

                    print("Found! SHA1 PASSWORD")
                    print("PASSWORD")
                    print("||||||||")
                    print('↓↓↓↓↓↓↓↓')
                    print(line.strip())
                    exit(0)
                
            elif type_of_hash == 'sha224':

                hash_object = hashlib.sha224(line.strip().encode())

                hashed_word = hash_object.hexdigest()

                if hashed_word == hash_to_decrypt:

                    print("Found! SHA224 PASSWORD")
                    print("PASSWORD")
                    print("||||||||")
                    print('↓↓↓↓↓↓↓↓')
                    print(line.strip())
                    exit(0)

            elif type_of_hash == 'sha256':
        
                hash_object = hashlib.sha256(line.strip().encode())

                hashed_word = hash_object.hexdigest()

                if hashed_word == hash_to_decrypt:

                    print("Found! SHA256 PASSWORD")
                    print("PASSWORD")
                    print("||||||||")
                    print('↓↓↓↓↓↓↓↓')
                    print(line.strip())
                    exit(0)

            elif type_of_hash == 'sha384':
            
                hash_object = hashlib.sha384(line.strip().encode())

                hashed_word = hash_object.hexdigest()

                if hashed_word == hash_to_decrypt:

                    print("Found! SHA384 PASSWORD")
                    print("PASSWORD")
                    print("||||||||")
                    print('↓↓↓↓↓↓↓↓')
                    print(line.strip())
                    exit(0)       

            
            elif type_of_hash == 'sha512':
                
                hash_object = hashlib.sha512(line.strip().encode())

                hashed_word = hash_object.hexdigest()

                if hashed_word == hash_to_decrypt:

                    print("Found! SHA512 PASSWORD")
                    print("PASSWORD")
                    print("||||||||")
                    print('↓↓↓↓↓↓↓↓')
                    print(line.strip())
                    exit(0) 

            elif type_of_hash == 'blake2b':
                
                hash_object = hashlib.blake2b(line.strip().encode())

                hashed_word = hash_object.hexdigest()

                if hashed_word == hash_to_decrypt:

                    print("Found! blake2b PASSWORD")
                    print("PASSWORD")
                    print("||||||||")
                    print('↓↓↓↓↓↓↓↓')
                    print(line.strip())
                    exit(0) 

        print("Password Not in File please expand file")

else:

    print("There is no such an arqument please make sure you to give true argument to program")