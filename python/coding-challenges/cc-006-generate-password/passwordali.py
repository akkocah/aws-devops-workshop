import random

error = "Please enter a valid name!!"
def generator(name):
    passwd = []
    name = name.lower().replace(" ","")
    if name == "" or not name.isalpha():
        return error
    for i in range(3):
        passwd.append(random.choice(name))
    for j in range(4):
        passwd.append(str(random.randint(0, 9)))
    return "".join(passwd)

while True:
    f_name = input("Please enter your full name: ")
    if f_name == "exit":
        print("Exiting Generator...")
        break
    print(generator(f_name))
    
