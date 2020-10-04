#! /bin/bash

# -e dosya mevcut
# -f dosya mevcut ve regular file
# -s dosya içeriği dolu
# -d klasör olup olmadığı
# -r read
# -w write
# -x executable


echo -e "dosyanıın ismini giriniz:\c"

read dosyaismi

if [ -e $dosyaismi ]  # buradaki e existmi anlamında
then
    echo "$dosyaismi bulundu"
else
    echo "dosyaismi bulunmadı"
fi

echo -e "dosyanıın ismini giriniz:\c"

read dosyaismi

if [ -s $dosyaismi ]  # buradaki e dosya içeriği dolumu anlamında anlamında
then
    echo "$dosyaismi içeriği dolu"
else
    echo "içeriği boş"
fi