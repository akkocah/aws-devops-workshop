print("###  This program converts milliseconds into hours, minutes, and seconds ###\n")
print("""(To exit the program, please type "exit")\n""")
def main():
    while True:
        millis = input("Please enter the milliseconds (should be greater than zero) :")
        if millis.lower() == "exit":
            print("Exiting the program... Good Bye")
            break
        if not millis.isdecimal() or int(millis) < 1:
            print("\nNot Valid Input !!!\n")
            continue

        if millis.isdecimal():
            millis = int(millis)
            miller = millis%1000
            seconds=(millis/1000)%60
            seconds = int(seconds)
            minutes=(millis/(1000*60))%60
            minutes = int(minutes)
            hours=(millis//(1000*60*60))                           

            print(f'{hours} hour/s'*(hours >= 1) + f' {minutes} minute/s'*(minutes != 0) + f' {seconds} second/s' *(seconds != 0) or f'just {miller} millisecond/s' * (miller < 1000),"\n",("%d:%d:%d:%d" % (hours, minutes, seconds,miller)))
            
            #print ("%d:%d:%d:%d" % (hours, minutes, seconds,miller))
main()

