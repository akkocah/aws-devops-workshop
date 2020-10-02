phonebook = {}
print("Welcome to the phonebook application\n\
Warning: This application is case sensitive!!!\n\
if you want to quit, please write 'quit' \n")


while True:
    inp = input("\n1. Find phone number\n\
2. Insert a phone number\n\
3. Delete a person from the phonebook\n\
4. Terminate\n\
Select operation on Phonebook App (1/2/3) :")
    if not inp.isdigit() or not 0 < int(inp) < 5:
        print("\nInvalid input format, please enter valid number\n")
    else: 
        if int(inp) == 4:
            print("\nExiting Phonebook...\n")
            phonebook.clear()
            break
        elif int(inp) == 2:
            name = input("Insert name of the person: ").strip()
            phone = input("Insert phone number of the person: ").strip()
            if name in phonebook.keys():
                print(f"\n{name} already exists.\n")
            elif not phone.isdigit() or len(phone) == 0 or len(phone) > 11:
                print("\nInvalid input format, cancelling operation ...\n")
            elif not name == "":
                phonebook[name] = phone
                print(f"\nPhone number of {name} is inserted into the phonebook\n")
            else:
                print("\nInvalid input format, cancelling operation ...\n")
        elif int(inp) == 1:
            search = input("Find the phone number of : ").strip()
            if search in phonebook.keys():
                print(f"\nThe number of {search} is: {phonebook[search]}")
            elif search == "":
                print("\nInvalid input format, cancelling operation ...\n")
            else:
                print(f"\nCouldn't find phone number of {search}\n")
        elif int(inp) == 3:
            remv = input("Whom to delete from phonebook: ").strip()
            if remv in phonebook.keys():
                phonebook.pop(remv)
                print(f"\n{remv} is deleted from the phonebook\n")
            else:
                print("\nInvalid input format, cancelling operation ...\n")
            
            
            

