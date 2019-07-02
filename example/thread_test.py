import time
import threading

def test(command="command"):
    i = 0
    while i<5:
        print(command+str(i))
        i+=1

def test2(video="asasd"):
    for i in range(11,20):
        print(video+str(i))

def test3(t):
    print(str(t))

a = threading.Thread(target=test,args=('hiloooo',))
d = threading.Thread(target=test)
b = threading.Thread(target=test2)
c = threading.Thread(target=test3,args=(5,))

a.start()
d.start()
c.start()
b.start()

