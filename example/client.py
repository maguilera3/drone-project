import socket

client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

for i in range(10):
	client.sendto(bytes(str(i)+"\n","utf-8"),("192.168.1.101",9999))
	recv = str(client.recv(1024),"utf-8")
	print("sent: Prueba\n")
	print("Received: ()".format(recv))
