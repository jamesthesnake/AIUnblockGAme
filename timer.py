import time
lastTime= 0


def timer():
  for x in range(50):
      global lastTime;
      print(time.time()-lastTime)*70000
      time.sleep(.5)
      lastTime=time.time()
