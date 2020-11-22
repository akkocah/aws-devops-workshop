hastag = int(input("Please enter the number"))

if hastag == 1:
    print("#")
else:
    print("#" * hastag)
    for i in range(hastag-2):
        print("#" + " " *(hastag-2) + "#")
    print("#" * hastag)
    
