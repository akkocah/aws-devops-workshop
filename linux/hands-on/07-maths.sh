#! /bin/bash

echo 1+1

echo $(( 1+1 ))

sayi1=25
sayi2=5

echo $(( sayi1+sayi2 ))
echo $(( sayi1-sayi2 ))
echo $(( sayi1*sayi2 ))
echo $(( sayi1/sayi2 ))
echo $(( sayi1%sayi2 ))

echo $( expr $sayi1 + $sayi2)
echo $( expr $sayi1 \* $sayi2) # expr kullanınca * için \* kullan

echo $(( $sayi1*$sayi2 ))

#######################  float numbers ###########
echo "==================="

echo "20.5+5"
echo "20.5+5" | bc
echo "20.5-5" | bc
echo "20.5*5" | bc
echo "20.5/5" | bc  #sonucu tam dönmedi bunun için scale kullan
echo "20.5%5" | bc

echo "scale=2;20.5/5" | bc

sayi1=20.5
sayi2=5

echo "scale=2;$sayi1/$sayi2" | bc

echo "scale=8; sqrt($sayi2)" | bc -l
echo "scale=2; $sayi2^3" | bc -l




