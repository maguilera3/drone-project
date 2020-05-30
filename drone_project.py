from flask import Flask, request
from flask_restful import Resource, Api
import socket
import threading
import time

app = Flask(__name__)
api = Api(app)

host = ''
port = 9001
locaddr = (host,port)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
tello_ip = '192.168.10.1'
tello_address = (tello_ip, 8889)
sock.bind(locaddr)

video_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#video_socket.bind(('0.0.0.0', 11111))

def command(command='command'):
    global sock
    if command=='command':
        while True:
            sock.sendto(command.encode(encoding="utf-8") , tello_address)
            time.sleep(5)
    else:
        sock.sendto(command.encode(encoding="utf-8") , tello_address)
        """
        if command=='streamon':
            threading.Thread(target=video).start()
            """

def video():
    """
    global video_socket
    global server_socket
    while True:
        msg, ip = video_socket.recvfrom(2048)
        server_socket.sendto(msg,('190.170.126.6',9999))
"""

class Control(Resource):
    def get(self):
        command_data = request.args['command']
        if not command_data=='land':
            threading.Thread(target=command,args=(command_data,)).start()
            threading.Thread(target=command).start()
        else:
            threading.Thread(target=command,args=('land',)).start()


api.add_resource(Control, '/control')

if __name__=='__main__':
    app.run('0.0.0.0',5000)
