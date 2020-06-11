num = int(input("Enter a number:"))
count=0
for n in range(1,num+1):
    if num%n == 0:
        count+=1
    if count >2:
        print("Composite number")
        break
else:
    print("Prime Number")
