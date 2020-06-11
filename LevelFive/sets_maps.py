
pra ={1,2,3,4} #Sets
print(pra)

def squareit(num):
    return num*num


result =map(squareit,pra)
# print(result)
actualR =set(result)
print(actualR)