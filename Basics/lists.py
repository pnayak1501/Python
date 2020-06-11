# Lists

myListOne = [3.14, "Prahlad", 6]
myListTwo = [4.65, "Prati", 8]

myListOne.append("john")
print(myListOne[1:1])
print(myListOne)
print(myListTwo)

print(myListOne[1])
print(myListOne[1:])

print(myListOne*2)
print(myListOne+myListTwo)

print(myListOne[1]+" "+myListTwo[1])

x = input("Enter the replacement:");
myListOne[1] = myListTwo[1] = x
print(myListOne)
print(myListTwo)

