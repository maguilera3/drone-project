import socketserver

package = 0
class UDP(socketserver.BaseRequestHandler):
	def handle(self):
		global package
		data = self.request[0].strip()
		socket = self.request[1]
		print("() wrote: ".format(self.client_address[0]))
		print(package)
		package+=1
		socket.sendto(data.upper(),self.client_address)

server = socketserver.UDPServer(('192.168.1.101',9999),UDP)
server.serve_forever()
