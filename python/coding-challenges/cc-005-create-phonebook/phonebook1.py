
print("Welcome to the phonebook application\n\
Warning: This application is case sensitive!!!\n\
if you want to quit, please write 'quit' \n")

phonebook = {}

def addRecord():
    name = input("\nInsert name of the person: ")
    number = input("Insert phone number of the person:")
    if not number.isdecimal() or number == "" or name == "":
        print("\nPlease enter the valid input format")
        
    elif name not in phonebook.keys():
        phonebook[name] = number
        #phonebook.update(name : number)
        print(f"\nPhone number of {name} is inserted into the phonebook\n")
    else:
        print(f"\n{name} already exists.\n")
    print(phonebook)

def findRecord():
    search = input("\nPlease enter the name to find the phone number of : ").strip()
    
    if search in phonebook.keys():
        print(f"\nThe number of {search} is: {phonebook[search]}")
    elif search == "":
        print("\nInvalid input format, cancelling operation ...\n")
    else:
        print(f"\nCouldn't find phone number of {search}\n")

def delRecord():
    remove = input("\nWhom to delete from phonebook: ").strip()
    if remove in phonebook.keys():
        phonebook.pop(remove)
        print(f"\n{remove} is deleted from the phonebook\n")
    else:
        print(f"\n{remove} is not found int the phonebook\n")

while True:
    process = input("\n1. Find phone number\n2. Insert a phone number\n\
3. Delete a person from the phonebook\n4. Terminate\n\
Select operation on Phonebook App (1/2/3/4) :")
    
    if process.lower() == "exit" or process == "4":
        print("çıkılıyor")
        break
    elif (not process.isdigit() or not 0 < int(process) < 5):
        print("\nInvalid input format, please enter valid number\n")
    if process == "1":
        findRecord()
    elif process == "2":
        addRecord()
    elif process == "3":
        delRecord()
   