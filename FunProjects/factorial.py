f = int(input("Enter a number: "))
fac=1;
# for i in range(f,1,-1):
#     fac=fac*i

while(f>0):
    fac=fac*f
    f-=1


print(fac)