from datetime import datetime
import random

# IP            Time                    URL                        Status
# 10.128.2.1    29/Nov/2017:06:58:55   GET /login.php HTTP/1.1     200
def create_log():
    IP = '.'.join(map(lambda x: str(random.randrange(1,256)), range(4)))
    TIME = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    URL = random.choice(["GET", "POST"])
    LOG = f"'{IP}', '{TIME}', '{URL}'"
    return LOG

if __name__ == '__main__' :
    for i in range(10) :
        print(create_log())