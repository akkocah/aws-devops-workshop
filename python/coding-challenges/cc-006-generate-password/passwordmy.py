# The purpose of this coding challenge is to write a program that creates a random password from a given full name.
import random

while True:
    name = input("enter your name and surname without spaces : ").replace(" ","")      
    if not name.isalpha():
        print("please enter the only alpha charecter")
        continue
    else:
        result = random.sample(name,3) + random.sample(range(1,10),4)
        print(result)

        password = "".join(map(str, result))
        print(f"Girilen kullanıya ait password : {password}")
        break
 


