import threading
def gfg():
    print("GeekforGeeks\n")

timer = threading.Timer(10.0,gfg)
timer.start()
print("Exit\n")