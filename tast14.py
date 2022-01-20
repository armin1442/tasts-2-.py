import time
from turtle import circle
from termcolor import colored

start = time.time()
number = 0
for i in range(100000000):
    number  += i

print(circle("Finished","green"))  
print(f"Ellapsed time: {time.time() - start} s")  