On start-up:
- The server starts listening on port 5021
- The server prints out a command for the client to run to connect to the server

Example Server Input:

1) Connect Base
cmd: connectbase userid pasid address port
purpose: Allow a new client to connect to the server
action: 
  - Generate new credentials for the client. 
  - Listen for new client connections. 
  - Process command from client.
  - Validate credentials
  - Sends back "correct" or "incorent"

2) Add Server Group
cmd: addservergroup RAM TEMPLATE SERVERLIMIT NAME 

purpose: add a server Group
actions
- tells availible base to start servers needed
- base starts needed servers



Example Client Input:
connectcore bc58ff7a-32bf-49fe-bddc-c2ecfb00d002 fbff20ae-5b43-4345-a02f-2e3b71b55b3d 127.0.0.1 5021

