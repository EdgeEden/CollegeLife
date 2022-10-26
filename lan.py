import os
import time

while True:
    res = os.system('ping 8.8.8.8')
    if res:
        os.system('Rasdial 宽带连接 /DISCONNECT')
        os.system('Rasdial 宽带连接 账号 密码')#  删掉“账号”两字后在原处输入宽带账号 密码同理
        time.sleep(5)
        pass
    else:
        print('网络已连接')
        time.sleep(5)
        break
