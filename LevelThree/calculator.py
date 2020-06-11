def add(num1, num2):
    return num1+num2


def sub(num1, num2):
    return num1-num2


def mul(num1, num2):
    return num1*num2


got = int(input(" 1. Add 2. Subtract 3. Multiply"))

num1 = int(input("Enter two numbers:"))
num2 = int(input("Enter two numbers:"))


if got == 1:
    print(add(num1,num2))
if got == 2:
    print(sub(num1, num2))
if got == 3:
    print(mul(num1, num2))


