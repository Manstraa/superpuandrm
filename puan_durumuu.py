#adim 1 : fonksiyon olustur
#adim 2  : girdilerini olustur
#adim 3 : girfilerin ciktilari olsun if kullan



def team():
    girdi = input('Takiminizin  Puanini Girin : ')
    if girdi==60 :
        print('Takiminiz Trabzon 1. sirada')
    elif girdi==41 :
        print('Takiminiz Besiktas 41 kere Masallah')
    if girdi==49:
        print('Takiminiz Mevlananin Memleketi')
    elif girdi==43 :
        print('Takiminiz Basaksehir')
print(team())