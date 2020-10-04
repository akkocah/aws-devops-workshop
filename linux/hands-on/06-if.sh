#! /bin/bash

# sayi=10

# if [ $sayi -eq  10 ]
# then
# echo "Koşul doğgru"
# fi

# if (( $sayi < 9 ))
# then
# echo "sayı 9 dan küçük"
# elif (($sayi > 9))
# then
# echo "sayı 9 dan büyük"
# else
# echo "sayı dokuza eşit"
# fi

# ad=hasan

# if [ $ad == "hasan" ]
# then 
# echo "isim $ad"
# fi

# harf=a

# if [[ $harf == "b" ]]
# then
# echo "harf b dir"
# elif [[ $harf == "a" ]]
# then
# echo "harf a dır "
# else
# echo "harf a veya b değildir"
# fi

################################################

yas=28
if [ "$yas" -gt 18 ] && [ "$yas" -lt 30 ]
then
echo "Geçerli yas"
else
echo "geçersiz yaş"
fi

yas=40
if [ "$yas" -gt 18 -a "$yas" -lt 30 ]
then
echo "Geçerli yas"
else
echo "geçersiz yaş"
fi

yas=60
if [ "$yas" -gt 18 ] || [ "$yas" -lt 30 ]
then
echo "Geçerli yas"
else
echo "geçersiz yaş"
fi

yas=60
if [ "$yas" -gt 18 -o "$yas" -lt 30 ]
then
echo "Geçerli yas"
else
echo "geçersiz yaş"
fi