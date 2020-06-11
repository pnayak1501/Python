lowerRange = int(input("Enter first number: "))
upperRange = int(input("Enter second number: "))
for number in range(lowerRange,upperRange+1):
    for i in range(2,number):
        if number%i == 0:
            break
    else:
        print(number)