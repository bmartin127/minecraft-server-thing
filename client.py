#base
from re import S
import uuid
import socket

connected = False

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    def connect_core(USERID, PASID, ADDRESS, PORT):
            print("connecting")
            PORT = int(PORT)
            s.connect((ADDRESS, PORT))
            s.sendall(str.encode(USERID))
            data = s.recv(1024)
            print(data)
            if data.decode() == "correct":
                s.sendall(str.encode(PASID))
                data = s.recv(1024)
                print(data)
                if data.decode() == "correct":
                    print("connect succsesful")
                    connected = True
                    return("success")  
                else: 
                    print("failed to connect")
                    return("failed")
                    s.close()
            else:
                print("failed to connect")
                return("failed")
                s.close()
    USERID = "0"
    def getcommandtyped():
        global connected
        commandinput = input().split()
        commandtype = (commandinput[0])
        if commandtype == ("connectcore"):
            USERID = commandinput[1]
            PASID = commandinput[2]
            ADDRESS = commandinput[3]
            PORT = commandinput[4]

            if connected == False:
                connect_core(USERID, PASID, ADDRESS, PORT)
                connected = True
                print("connected state:",connected)
            else:
                print("core is already connected")
                print("wont make any changes")
    while 1 == 1:
        getcommandtyped()
    def senddata(datatosend):
        if connected == True:
            str.encode(USERID), s.sendall(str.encode(datatosend))