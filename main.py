from flask import Flask, request
from flask_restful import Resource, Api
import socket
import threading 
import time

app = Flask(__name__)
api = Api(app)

host = ''
port = 9000
locaddr = (host,port) 
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
tello_ip = '192.168.10.1'
tello_address = (tello_ip, 8889)
sock.bind(locaddr)

def command(command='command'):
    if command=='command':
        while True:
            sock.sendto(command.encode(encoding="utf-8") , tello_address)
            time.sleep(5)
    else:
        sock.sendto(command.encode(encoding="utf-8") , tello_address)
        
class Control(Resource):
    def post(self):
        command_data = request.form['command']
        if not command_data=='land':
            threading.Thread(target=command,args=(command_data,)).start()
            threading.Thread(target=command).start()
        else:
            threading.Thread(target=command,args=('land',)).start()

api.add_resource(Control, '/control')


