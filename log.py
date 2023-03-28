from datetime import datetime
import random
import time

URL_DIR = ['']

def create_log():
  IP = '.'.join(map(lambda x:str(random.randrange(1, 255)), range(4)))
  Time = datetime.now().strftime("%d/%B/%Y %H:%M:%S")
  URL = random.choice(["GET", "GET", "GET", "GET", "POST"])+(' HTTP/1.1')
  Staus = random.choice([200, 200, 200,200, 200, 200, 200, 200, 200, 200, 200, 200, 206, 302, 304, 404, 500])
  return IP, Time, URL, Staus

# IP              Time                    URL                    Staus
# 10.128.2.1   29/Nov/2017 06:58:55   GET /login.php HTTP/1.1   200

while True:
  print(create_log())

  time.sleep(1)