# # GÖREV 1: List Comprehension yapısı kullanarak car_crashes verisindeki numeric değişkenlerin isimlerini büyük harfe çeviriniz ve başına NUM ekleyiniz.
# ###############################################
#
# # Beklenen Çıktı
#
# # ['NUM_TOTAL',
# #  'NUM_SPEEDING',
# #  'NUM_ALCOHOL',
# #  'NUM_NOT_DISTRACTED',
# #  'NUM_NO_PREVIOUS',
# #  'NUM_INS_PREMIUM',
# #  'NUM_INS_LOSSES',
# #  'ABBREV']
#
# # Notlar:
# # Numerik olmayanların da isimleri büyümeli.
# # Tek bir list comp yapısı ile yapılmalı.

#%%


#Görev 1: List Comprehension yapısı kullanarak car_crashes verisindeki numeric değişkenlerin isimlerini büyük
#harfe çeviriniz ve başına NUM ekleyiniz
"""
import seaborn as sns
df=sns.load_dataset("car_crashes")


df.columns=["NUM_"+col.upper() for col in df.columns if df[col].dtype!="0"  ]
#object degilse  yani numericse
#  cikti  dongu  sart

df.columns


"""


#%%gorev 2

#Görev 2: List Comprehension yapısı kullanarak car_crashes verisinde isminde "no" barındırmayan
#değişkenlerin isimlerinin sonuna "FLAG" yazınız
import seaborn as sns
df=sns.load_dataset("car_crashes")

df.columns #-->column isimlerini gordum

[i.upper()+"_FLAG" for i in  df.columns if not "no" in df.columns ]








