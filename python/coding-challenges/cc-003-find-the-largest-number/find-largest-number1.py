# while True:
#     try:
#         numbers = map(int, input("Please enter the 5 number with spaces :").split())
#         numbers = sorted(list(numbers))
#         print(numbers)
#         print(f"the number is {numbers[-1]}")
#         print(f"the number is {sorted(list(numbers))[-1]}") 
#         break
#     except ValueError as e:
#         print(e, "lütfen sayı giriniz")
#     continue



# ########################################################

# n = 0
# a = []
# while n < 5:    
#     a.append(int(input("enter the the number : ")))
#     n += 1
# print(a)
# print(f"the largest number is {sorted(a)[-1]}")

# #####################################################

# b = []
# for i in range(5):
#     b.append(int(input("enter the the number : ")))
# print(b)
# print(f"the largest number is {sorted(b)[-1]}")

###################################

n = 0
mylist = []
while n < 5:    
    num = input("enter the the number : ")
    if not num.isdecimal():
        pass     
    else:
        mylist.append(int(num)) 
        n += 1
#print(mylist)
print(f"the largest number is {sorted(mylist)[-1]}")

#####################################################

num_list = []
for i in range(5):
    num = input("Enter a number: ")
    num_list.append(num)
max_list = []
for i in num_list:
    if max_list == []:
        max_list.append(int(i))
    if int(i) > max_list[0]:
        max_list[0] = int(i)
print(max_list[0])   