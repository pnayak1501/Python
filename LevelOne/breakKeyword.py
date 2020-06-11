listOne = [23, 32, 323, 332, 31, 321, 445, 3]

# user_in = int(input("Enter a number: "))
# checker = False
#
# for a in listOne:
#     if a == user_in:
#         print("Match Found")
#         break
#     else:
#         print("Match NOT Found")

# METHOD 2
# checker = False
# while checker == False:
#     user_in = int(input("Enter a number: "))
#     for a in listOne:
#         if a == user_in:
#             print("Match Found")
#             checker = True
#             break
#     else:
#         print("NOT FOUND")

for i in list(range(0,5)):
    listOne[i] = i*i;

print(listOne)