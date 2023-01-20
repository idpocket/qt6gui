import threading
from  threading import Thread



def qq():
    for _ in range(10):
        print(_)

t1 = threading.Thread(target=qq)
t2 = threading.Thread(target=qq)

t1.start()
t2.start()
t1.join()
t2.join()