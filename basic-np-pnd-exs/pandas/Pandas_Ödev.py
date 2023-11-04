# %%Pandas Odev

import pandas as pd

df = pd.read_csv("heart.csv")

df.info()
describe = df.describe().T

# Ozellik Bilgisi:

# yas
# seks(Cinsiyet)
# gogus agrisi tipi (4 deger)
# dinlenme kan basıncı
# mg / dl olarak serum kolestoral
# aclik kan sekeri> 120 mg / dl
# dinlenme elektrokardiyografik sonuclari (degerler 0,1,2)
# elde edilen maksimum kalp atis hizi
# egzersize bagli anjina
# oldpeak = egzersize gore egzersize bagli ST depresyonu
# pik egzersiz ST segmentinin egimi
# floroskopi ile renklendirilmis buyuk damar (0-3) sayisi
# thal: 3 = normal; 6 = sabit kusur; 7 = tersinir kusur


#%% Soru1 -> Dataya "Ulke" adinda bir sutun ekleyin.Ulke sutununun aldigi degerler ["Turkiye","Almanya"] istediginiz oranda yerlestirebilirsiniz.

df["ulke"]=[ "isvec" if i <100 else "turkiye" for i in df.index]
df.ulke
#%% Soru2 -> Bu veri kumesinde kac erkek ve kadin ( cinsiyet ozelligi) temsil edilmektedir?


df.sex.value_counts()

#%% Soru3 -> Kadinlarin ortalama yasi nedir?
df[df.sex==0].mean()
#%% Soru4 -> Verisetindeki 'trestbps','thal' sutunlarini silin.
cols=['trestbps','thal']

df.drop(cols,axis=1)
#%% Soru5 -> En yuksek yasa sahip olan kisinin hasta olup olmadigini bulunuz.
yasli=df.age.max()
df[df.age==yasli]["target"]
#%% Soru6 -> En dusuk yasa sahip olan kisinin hasta olup olmadigini bulunuz.
genc=df.age.min()

df[df.age==genc]["target"]
#%% Soru7 -> isvec vatandaslarinin yuzdesi nedir?
df[df.ulke=="isvec"].count()/(df[df.ulke=="isvec"].count()+df[df.ulke=="turkiye"].count())*100
# %% Soru8 -> Kanser olanlarin yas ortalamsi ve standat sapmasi nedir?
k=df[df["target"]==1]
k["age"].agg(["mean","std"])
#%% Soru9 -> Kanser olanlarin en az cp değeri 1 oldugu dogru mudur?
k["cp"].min() #no
#%% Soru10 -> Her irk ve her cinsiyet  icin yas istatistiklerini goruntuleyin.or: Max,min,mean.
i=df[df["ulke"]=="isvec"]

i["age"].mean()
i["sex"].value_counts()

t=df[df["ulke"]=="turkiye"]

i["age"].mean()
#%% Soru11 -> Her ulke icin hasta olanlarin yas istatistiklerini goruntuleyin.
k=df[df["target"]==1]

k.age.describe()
# %% Soru12 -> Max "ca" degeri nedir? Bu degerde olan kac kisi var?
df.ca.max()

df[df.ca==4] #5
#%% Soru13 -> Max "ca" olup hasta olanlarin yuzdesi nedir?
o=df[df.ca==df.ca.max()].count()
(o/df["ca"].shape[0])*100
df["ca"].shape[0]
#%% Soru14 -> 60 yas ustune "yasli" digerlerine "genc" olmak uzere yeni bir sutun olusrunuz.

def yas(i):
    if i<60:
        return "genc"
    else:
        return "yasli"


df.age.apply(yas)























