#core
data = 0
conn = 0
from dataclasses import dataclass
import socket
import uuid
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    def connect_base():
        HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
        PORT = 5021  # Port to listen on (non-privileged ports are > 1023)

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            USERNAME = str(uuid.uuid4())
            PASSWORD = str(uuid.uuid4())
            print("username:", USERNAME,)
            print("password:", PASSWORD)
            print("connecting to:", PORT)
            print("waiting for connectoin use the command","{connectcore",USERNAME,PASSWORD,HOST,PORT,"}to connect")
            s.bind((HOST, PORT))
            s.listen()
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                data = conn.recv(1024)
                print("Just recieved data: {}".format(data))
                if (data.decode()).strip() == USERNAME.strip():
                    conn.sendall(b"correct")
                    print("username correct")
                    data = conn.recv(1024)
                    print("compare: **",(data.decode()).strip(),"**",PASSWORD.strip(),"**")
                    if (data.decode()).strip() == PASSWORD.strip():
                        conn.sendall(b"correct")
                        print("password correct")
                        print("connect succsesfully")
                    else:
                        conn.sendall(b"incorrent")
                        print("password incorrect")
                        print(data.decode(),"was used for password")
                else: 
                    conn.sendall(b"incorent")
                    print("username incorrect")
                    print(data.decode(),"was used for username")

    def getcommandtyped():
        commandinput = input().split()
        commandtype = (commandinput[0])
        if commandtype == ("connectbase"):
            connect_base()
            
    while 1 == 1:
        getcommandtyped()

    while 1 == 1:
        data = conn.recv(1024)
        print("Recieved data {}".format(data))
        if data.decode() == "disconnect":
            s.close()

            

            


