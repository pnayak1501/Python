import random

def magic():
    for i in range(6):
        yield random.randrange(1,20)


for number in magic():
    print("Value is ",number)