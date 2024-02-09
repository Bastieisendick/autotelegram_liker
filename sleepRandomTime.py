import time
import random


def randSeconds(minSeconds, maxSeconds, decimals=3):

    return round(random.uniform(minSeconds, maxSeconds), decimals)



def sleepRand(minSeconds, maxSeconds, decimals=3):

    time.sleep(randSeconds(minSeconds, maxSeconds, decimals))


