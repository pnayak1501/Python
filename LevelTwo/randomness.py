import random

print(random.choice([1,2,3,4,5,6]))
print(random.choice(range(1,7)))
print(random.choice("PrahladNayak"))
print(random.randrange(1,100,2))
print(random.random())

list_num = [2, 3, 4, 32, 132]
random.shuffle(list_num)
print(list_num)