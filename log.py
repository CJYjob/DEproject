from datetime import datetime
import random
import time



STAUS = [200, 200, 200,200, 200, 200, 200, 200, 200, 200, 200, 200, 206, 302, 304, 404, 500]

def create_log():
  with open('url.txt') as f:
    randomLine = random.choice(list(f.readlines()))
    f.close()

  IP = '.'.join(map(lambda x:str(random.randrange(1, 255)), range(4)))
  Time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
  URL = randomLine.splitlines()[0]
  Staus = random.choice(STAUS)
  return IP, Time, URL, Staus

# IP              Time                    URL                    Staus
# 10.128.2.1   29/Nov/2017 06:58:55   GET /login.php HTTP/1.1   200

while True:
  print(create_log())

  time.sleep(1)