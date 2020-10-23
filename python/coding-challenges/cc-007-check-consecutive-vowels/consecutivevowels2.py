
str = list(input("Please enter the text :").lower())
vow = ["a","e","i","u","o"]

lst = [[str[i-1], str[i]] for i in range(1,len(str)) if str[i] in vow if str[i-1] in vow]

print(f"{'positive'}" * (len(lst)!=0) + f"{'negative'}" * (len(lst)==0))


