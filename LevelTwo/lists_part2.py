marvel =["Superman", "Spiderman","Ironman"]
cricket=["Sachin","Dhoni"]
marvel.append("Black Widow")
print(marvel)
marvel.remove("Superman")
print(marvel)
marvel.insert(1, "Superman")
print(marvel)
marvel.reverse()
print(marvel)

print(marvel.count("Spiderman"))
print(marvel+cricket)

marvel.extend(cricket)
print(marvel)