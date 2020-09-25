#!/bin/bash
number=10
let new_number=number++
echo "Number: $number"
echo "N.Num: $new_number"
sayi=10
let yenisayi=--sayi
echo $sayi
echo $yenisayi

9:01
********************
9:01
#!/bin/bash
number=10
let new_number=number++
echo "Number: $number"
echo "N.Num: $new_number"
sayi=10
let yenisayi=--sayi
echo $sayi
echo $yenisayi
[ec2-user@ip-172-31-92-34 ~]$ ^C
[ec2-user@ip-172-31-92-34 ~]$ cat exer.sh
#!/bin/bash
read -p "first number: " num1
read -p "second number: " num2
let total=num1+num2
echo $(( total++ ))
echo $total
echo $(( total - num1 ))
9:01
*************
9:01
cat exer2.sh
#!/bin/bash
read -p "kaç yaşındasın? " age
if [ $age -ge 16 ]
then
        echo "araba sürebilirsin."
elif [ $age -eq 15 ]
then
        echo "önümüzdeki yıl sürebilirsin"
else
        echo "araba süremezsin"
fi
[ec2-user@ip-172-31-92-34 ~]$ cat exer2.sh
#!/bin/bash
read -p "kaç yaşındasın? " age
if [ $age -ge 16 ]
then
        echo "araba sürebilirsin."
elif [ $age -eq 15 ]
then
        echo "önümüzdeki yıl sürebilirsin"
else
        echo "araba süremezsin"
fi
9:02
*********************
9:02
cat exer3.sh
#!/bin/bash
read -p "kaç yaşındasın? " age
if (( age >= 16 ))
then
        echo "araba sürebilirsin."
elif [ $age -eq 15 ]
then
        echo "önümüzdeki yıl sürebilirsin"
else
        echo "araba süremezsin"
fi
9:02
*****************
9:02
cat log.sh
#!/bin/bash
read -p "enter number 1: " n1
read -p "enter number 2: " n2
read -p "enter number 3: " n3
if (( (( n2 > n1 )) && (( n2 < n3 )) ))
then
        echo "$n2 is between $n1 and $n3"
elif (( (( n1 > n2 )) || (( n3 < n2 )) ))
then
        echo "$n2 is out of range"
fi
9:02
************
9:02
cat calculate.sh
#!/bin/bash
base_value=5
read -p "Enter a number: " user_input
total=$((base_value+user_input))
echo "Total value is: $total"
9:03
******************
9:03
#!/bin/bash
echo "Hello World"
date
echo "more then enough"
9:03
**************
9:03
cat mycopy.sh
#!/bin/bash
cp $1 $2
echo kopyalanan dosya detayları $2
ls -lh $2