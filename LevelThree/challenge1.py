def remove(*num):
    total=100
    for n in num:
        total=total-n

    return total


print(remove(1,2,3,4,5,6))