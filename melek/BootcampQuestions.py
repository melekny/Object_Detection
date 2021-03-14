# 1.Soru: Kullanıcıdan aldığı iki sayı ile toplama, çıkartma, çarpma ve bölme işlemlerini yapan programı kodlayınız.

# Çözüm-1

sayi1=int(input("Birinci sayıyı giriniz: "))
sayi2=int(input("İkinci sayıyı giriniz: "))
islem=input(" Yapmak istediğiniz işlemi seçiniz (+,-,*,/): ")
 
if islem=="+":
    sonuc=sayi1+sayi2
    print(sonuc)
elif islem=="-":
    sonuc=sayi1-sayi2
    print(sonuc)
elif islem=="*":
    sonuc=sayi1*sayi2
    print(sonuc)
elif islem=="/":
    sonuc=sayi1/sayi2
    print(sonuc)
else:
    print("Yanlış işlem girdiniz")

 

# 2.Soru: Klavyeden maaşı ve zam oranı girilen kişinin zamlı maaşını hesaplayan Python kodunu yazınız.

# Çözüm-2

yeniMaas=0
maas = input("Maaşı Gir : ")
zam = input("Zam Oranı(%) : ")

yeniMaas = int(maas) + (int(maas) * int(zam)/100)
print("Zamlı Maaş :",yeniMaas)
 


# 3.Soru: Bir üçgenin iç açıları toplamı 180 derecedir. Kullanıcıdan alınan üç açı değerine göre “Bu bir üçgendir.” ya da “Bu bir üçgen değildir.” çıktılarını veren kodu yazınız.

# Çözüm-3

aci1= int(input('1. AÇI : '))
aci2=int(input('2. AÇI : '))
aci3=int(input('3. AÇI : '))
toplam = aci1 + aci2 + aci3
 
if toplam ==180 :
  print("Bu bir üçgendir.")
else:
  print("Bu bir üçgen değildir.")



# 4.Soru: Girilen saniye bilgisine göre; saat-dakika-saniye bilgisini yazdıran Python kodunu yazınız.

# Çözüm-4

saniye = int (input ("Saniye giriniz:"))

saat = saniye // 3600
saniye = saniye % 3600
dakika = saniye // 60
saniye = saniye % 60

print("Girdiğiniz Saniyenin Saat Dönüşümü:",saat,"sa",dakika,"dk",saniye,"sn")



# 5.Soru: Klavyeden boy ve kilo bilgileri girilen kişinin beden kitle endeksini hesaplayan python kodunu yazınız.
# Beden Kitle İndeksi= kilo/(boy**2)

# Çözüm-5

boy=float(input("Boyunuzu giriniz(m): "))
kilo=float(input("Kilonuzu giriniz(kg): "))
bki=kilo/(boy**2)
print("Beden Kitle İndeksi Değeriniz:",round(bki,2))



# 6.Soru: Kullanıcının girdiği Santigrat derece değerine göre; Fahrenheit ve Kelvin dönüşümlerini hesaplayan Python kodunu yazınız.
# Dönüşüm Formülleri: Santigrat-Fahrenheit  F = 9/5 (° C) + 32 |  Santigrat-Kelvin  K = ° C + 273 

# Çözüm-6

deg = float(input("Santigrat derece giriniz:"))
 
fah = deg * 1.8 + 32;
kelvin = deg + 273;
 

print("Fahrenait Değeri= ",fah)
print("Kelvin Değeri= ",kelvin)



# 7.Soru: Bakiye sorgulama, para çekme ve yatırma, çıkış işlemlerini içeren basit bir ATM uygulamasını kodlayınız.

# Çözüm-7

print("""

ATM uygulamasına hoş geldiniz.!
(1) Bakiye Sorma
(2) Para Çekme
(3) Para Yatırma
(q) Çıkış

""")

bakiye = 1000

while True:
    islem = input("Lütfen yapmak istediğiniz işlemi seçiniz: ")
    if islem == "q":
        print("İyi Günler Dileriz...")
        break
    elif (islem == "1"):
        print("Bakiye: {}".format(bakiye))

    elif (islem == "2"):
        tutar = int(input("Ne kadar para çekmek istiyorsunuz: "))
        
        if (bakiye - tutar < 0):
            print("Yetersiz bakiye...")
            continue
        bakiye -= tutar

    elif (islem == "3"):
        tutar = int(input("Ne kadar para yatırmak istiyorsunuz: "))
        bakiye = bakiye + tutar
        print("Yeni bakiyeniz: {}".format(bakiye))
    else:
        print("Geçersiz işlem girdiniz..!")



# Bonus Soru: Taş-Kağıt-Makas oyununu Python ile kodlayınız.

# Çözüm

import random
import sys
 
secenek = ["Taş","Kağıt","Makas"]
taş = secenek[0]
kağıt = secenek[1]
makas = secenek[2]
oyuncu_skor = 0
bilg_skor = 0
 
def oyuncu_sonuc(oyuncu_skor,bilg_skor):
    if oyuncu_skor == 3:
        print("Senin puanın: {} , Bilgisayarın puanı: {}\n".format(oyuncu_skor, bilg_skor))
        print("Oyun bitti. Kazandınız!!!")
        sys.exit()
    else:
        print("Bilgisayar {} seçti, sonuç: Kazandınız".format((bilg_secim)))
        print("Senin puanın: {} , Bilgisayarın puanı: {}\n".format(oyuncu_skor, bilg_skor))
    return
 
def bilg_sonuc(oyuncu_skor,bilg_skor):
    if bilg_skor == 3:
        print("Senin puanın: {} , Bilgisayarın puanı: {}\n".format(oyuncu_skor, bilg_skor))
        print("Oyun bitti. Kaybettiniz...")
        sys.exit()
    else:
        print("Bilgisayar {} seçti, sonuç: Kaybettiniz".format((bilg_secim)))
        print("Senin puanın: {} , Bilgisayarın puanı: {}\n".format(oyuncu_skor, bilg_skor))
    return
 
print("Taş-Kağıt-Makas oyununa hoş geldiniz. Oyundan çıkmak için x tuşuna basınız.\n3 skoruna ulaşan kazanır, bol şans!!!\n")
 
while True:
    bilg_secim = random.choice(secenek)
    secim = input("Sezgilerine güven. Taş mı kağıt mı makas mı? ")
    if secim == taş :
        if bilg_secim == taş :
            print("Bilgisayar taş seçti, sonuç: Berabere\n")
        elif bilg_secim == makas :
            oyuncu_skor += 1
            oyuncu_sonuc(oyuncu_skor,bilg_skor)
        else:
            bilg_skor += 1
            bilg_sonuc(oyuncu_skor,bilg_skor)
    elif secim == kağıt :
        if bilg_secim == kağıt :
            print("Bilgisayar kağıt seçti, sonuç: Berabere\n")
        elif bilg_secim == taş :
            oyuncu_skor += 1
            oyuncu_sonuc(oyuncu_skor,bilg_skor)
        else:
            bilg_skor += 1
            bilg_sonuc(oyuncu_skor,bilg_skor)
    elif secim == makas :
        if bilg_secim == makas :
            print("Bilgisayar makas seçti, sonuç: Berabere\n")
        elif bilg_secim == kağıt :
           oyuncu_skor += 1
           oyuncu_sonuc(oyuncu_skor,bilg_skor)
        else:
            bilg_skor += 1
            bilg_sonuc(oyuncu_skor,bilg_skor)
    else:
        if secim == "x" :
            print("Çıkılıyor...")
            break