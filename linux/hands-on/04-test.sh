#! /bin/bash

# echo $BASH
# echo $BASH_VERSION
# echo $HOME
# echo $PWD

# ad=hasan
# echo $ad
# sayi1=12
# sayi2=8

# echo $sayi1     
# echo $sayi2

# echo "isminiz"
# read isim 
# echo "ismim $isim"

# echo "isimler "
# read isim1 isim2 isim3
# echo "isimler: $isim1, $isim2, $isim3"

# read -p "isminizi giriniz " isim
# read -sp "şifrenizi giriniz" sifre
# echo "ismim $isim"
# echo "şifrem $sifre"

# echo "isminiz giriniz"
# read
# echo "ismim $REPLY"

# echo "isimler"
# read -a isimler
# echo "isimler: ${isimler[0]}, ${isimler[1]},${isimler[2]}"

# ARGUMENTS LOCAL VARIABLES
#echo $1 $2 $3 # buradaki değerleri tek tek girmeliyiz

echo $@   # bu ise girilen tüm argümanları döner
echo $*   # bu ise girilen tüm argümanları döner
echo $#  # argümanların sayısını gösterir

dizi=("$@")
echo ${dizi[0]} ${dizi[3]}