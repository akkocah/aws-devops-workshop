from random import choice, randint 
# Eğer önceden belirlediğimiz bir listeden rastgele bir eleman seçmek istiyorsak, bu durumda kullanacağımız metot choice metodudur.
# integer tipinde bir sayı istiyorsak bu durumda randint metodunu kullanabiliriz. Bu metot kullanılırken başlangıç ve bitiş aralık değerleri verilir; ancak bu durumda bitiş değeri de rastgele sayı olarak tutabilir. Yani [başlangıç, bitiş] aralığı kullanılır.

name = ''
name = input("Enter your name all lowercase ")
name_list = name.lower().split()
name_no = ''.join(name_list)

letters_list = [choice(name_no) for _ in range(3)]
numbers_list = [str(randint(0, 9)) for _ in range(4)]
password = ''.join(letters_list + numbers_list)
print(password)