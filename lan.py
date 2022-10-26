import os
import time

while True:
    res = os.system('ping 8.8.8.8')
    if res:
        os.system('Rasdial 宽带连接 /DISCONNECT')
        os.system('Rasdial 宽带连接 hzqta57196572 459630')
        time.sleep(5)
        pass
    else:
        print('网络已连接')
        time.sleep(5)
        break
