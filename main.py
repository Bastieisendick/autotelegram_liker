import time
from datetime import datetime


import messageLiker
from sleepRandomTime import sleepRand
from sleepRandomTime import randSeconds





formatted_time = datetime.now().strftime("%Y.%m.%d %H:%M:%S")

print("*************************************")
print("*                                   *")
print("* Auto Telegram Liker is running... *")
print("*                                   *")
print("*************************************")

print(f"Start Time: {formatted_time}")



while True:
    try:

        messageLiker.work(randSeconds(20000, 30000))
        sleepRand(7200, 14400)

    except:
        print("Error in main loop")
        time.sleep(300)
