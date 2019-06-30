#
# Tello Python3 Control Demo 
#
# http://www.ryzerobotics.com/
#
# 1/1/2018

import threading 
import socket
import sys
import time
import http.server
import socketserver

host = ''
port = 9000
locaddr = (host,port) 

# Web server HERE
PORT = 3000

Handler = http.server.SimpleHTTPRequestHandler
Handler.extensions_map.update({
    '.webapp': 'application/x-web-app-manifest+json',
});

httpd = socketserver.TCPServer(("", PORT), Handler)

print ("Serving at port", PORT)
#httpd.serve_forever()

serverThread = threading.Thread(target=httpd.serve_forever)
#serverThread.start()

#END WEBSERVER HERE


# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

tello_ip = '192.168.10.1'
tello_address = (tello_ip, 8889)

sock.bind(locaddr)

def recv():
    count = 0
    while True: 
        try:
            data, server = sock.recvfrom(1518)
            print(data.decode(encoding="utf-8"))
        except Exception:
            print ('\nExit . . .\n')
            break


print ('\r\n\r\nTello Python3 Demo.\r\n')

print ('Tello: command takeoff land flip forward back left right \r\n       up down cw ccw speed speed?\r\n')

print ('end -- quit demo.\r\n')


#recvThread create
recvThread = threading.Thread(target=recv)
#recvThread.start()

sent = sock.sendto('command'.encode(encoding="utf-8") , tello_address)
sent = sock.sendto('streamon'.encode(encoding="utf-8") , tello_address)
sent = sock.sendto('takeoff'.encode(encoding='utf-8'),tello_address)
sock.sendto('up 10'.encode(encoding='utf-8'),tello_address)
sock.sendto('down 10'.encode(encoding='utf-8'),tello_address)
sock.sendto('left 10'.encode(encoding='utf-8'),tello_address)
sock.sendto('right 10'.encode(encoding='utf-8'),tello_address)
print(sent)

def video():
    video_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    video_socket.bind(('0.0.0.0', 11111))
    
    i=0
    while i<10:
        msg, ip = video_socket.recvfrom(2048)
        server_socket.sendto(msg,('192.168.1.101',9999))
        i+=1
    sock.sendto('land'.encode(encoding='utf-8'),tello_address)
        

    

    
videoThread = threading.Thread(target=video)
videoThread.start()

while True: 

    try:
        msg = input("");

        if not msg:
            break  

        if 'end' in msg:
            print ('...')
            sock.close()  
            break

        # Send data
        msg = msg.encode(encoding="utf-8") 
        sent = sock.sendto(msg, tello_address)
    except KeyboardInterrupt:
        print ('\n . . .\n')
        sock.close()  
        break



