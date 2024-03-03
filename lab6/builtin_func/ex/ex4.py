import time
import math

def my_func(number, millisec):
    time.sleep(millisec/1000)
    return math.sqrt(number)

number=int(input())
millisec=int(input())
result=my_func(number,millisec)

print("square root of", number, "after", millisec, "millisecond is", result)