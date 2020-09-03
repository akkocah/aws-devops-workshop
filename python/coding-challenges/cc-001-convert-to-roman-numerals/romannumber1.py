
conv = [[1000, 'M'], [900, 'CM'], [500, 'D'], [400, 'CD'],
        [ 100, 'C'], [ 90, 'XC'], [ 50, 'L'], [ 40, 'XL'],
        [  10, 'X'], [  9, 'IX'], [  5, 'V'], [  4, 'IV'],
        [   1, 'I']]

print("###This program converts decimal numbers to Roman Numerals ### \n")
while True:
    while True:
        num= input('''(To exit the program, please type "exit")\n
Please enter a number between 1 and 3999, inclusively : ''')
        if num == "exit":
            print("Exiting the program... Good Bye")
            quit()
        elif num.isdigit() != True:
            print("Please enter the only INTEGER value \n")
        elif int(num) > 3999:
            print("Please enter the BETWEEN 1 and 3999 \n")
        elif int(num) <= 0:
            print("Please enter the BETWEEN 1 and 3999 \n")
        else:
            break
    num = int(num)
    roman = ''
    i = 0 #initiate i = 0
    while num > 0:
        while conv[i][0] > num:
            i+=1 #increments i to largest value greater than current num
        roman += conv[i][1] #adds the roman numeral equivalent to string
        num -= conv[i][0] #decrements your num        
    print(f"Your number is equal as Roman numerals: {roman}\n")
    
    


    