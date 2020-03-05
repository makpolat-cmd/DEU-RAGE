from time import sleep

print("Algoritma basladi.")

## kamera tanım
## motor tanım
## diğer tanımlamalar

while True : # ana döngü
   
    while True: # ilerleme döngüsü
        print("Ana Döngü.")
        sleep(0.5)
        durum=int(input("durumtespiti (1 , 2 veya 3) :")) ##durum tespiti
        if durum==1 or durum==2 or durum==3: #anormal durum kontrol
            #hiz yavaslatilabilir
            break

    if durum == 1 : # olası durum 1
        while True:
            
            #durum 1 yapilacak seyler
            
            print("Durum 1 döngüsü")
            durum1sonu = int(input("durum1sonu? :")) # durum1 sonu kontrol
            if durum1sonu == 1:
                #
                print("Durum 1 için gerekli şeyler yapıldı.")
                print("Ana döngüye giriliyor.")
                break

    elif durum == 2: # olası durum 2
        while True:
            
            #durum 2 yapilacak seyler
            print("Durum 2 döngüsü")
            
            durum2sonu = int(input("durum2sonu? :"))# durum2 sonu kontrol
            if durum2sonu== 1:
                #
                print("Durum 2 için gerekli şeyler yapıldı.")
                print("Ana döngüye giriliyor.")
                break
            

    elif durum == 3 : #olası durum 3
        while True:
            
            #durum 3 yapilacak seyler
            print("Durum 3 Döngüsü")
            durum3sonu = int(input("durum3sonu? :"))# durum3 sonu kontrol
            if durum3sonu == 1:
                #
                print("Durum 3 halledildi.")
                print("Ana döngüye giriliyor.")
                break
    
    if int(input("yarissonu? :"))==1:
                #
                print("yarisbitti")
                break
print("program bitti")