side_length = int(input("Enter a number: "))
if side_length == 1:
    print("*")
else:
    print("*" * side_length)
    for i in range(side_length-2):
        print("*" + " " * (side_length-2) + "*")
    print("*" * side_length)