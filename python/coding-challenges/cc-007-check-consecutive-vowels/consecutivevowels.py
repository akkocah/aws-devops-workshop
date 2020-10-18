
text = list(input("Please enter the text :").lower())
vowels = ["a","e","i","u","o"]
result=False

if len(text) <= 1:
    result = False
else:
    for i in range(len(text)-1):        
        if text[i] in vowels and text[i+1] in vowels:
            result = True
            break
if result:
    print("positive")
else:
    print("negative")



