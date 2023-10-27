# Görev17:  Seaborn kütüphanesi içerisinden Tipsveri setini tanımlayınız
#%%
import seaborn as sns

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
# df = sns.load_dataset("titanic") --> sil
df = sns.load_dataset("tips")


# Görev18:  Time değişkenininkategorilerine(Dinner, Lunch) göretotal_billdeğerlerinintoplamını, min, max veortalamasınıbulunuz.Görev19:  Günlerevetime göretotal_billdeğerlerinintoplamını, min, max veortalamasınıbulunuz
df.head()
df.groupby("time").agg({"total_bill":["sum","max","min","mean"]})

# Görev19:  Günlerevetime göretotal_billdeğerlerinintoplamını, min, max veortalamasınıbulunuz.Pandas Alıştırmalar
df.groupby(["day","time"]).agg({"total_bill":["sum","max","min","mean"]})

# Lunch zamanına ve kadın müşterilere ait total_bill ve tip değerlerinin day'e göre toplamını, min, max ve ortalamasını bulunuz
df.head()
#%%
# Görev 20: Lunch zamanına ve kadın müşterilere ait total_bill ve tip değerlerinin day'e göre toplamını, min, max ve ortalamasını bulunuz
kadinveLunch=df.loc[(df["sex"]=="Female") & (df["time"]=="Lunch")]

kadinveLunch.groupby("day").agg(["min","max","mean"])

#########################################
# Görev 21: size'i 3'ten küçük, total_bill'i 10'dan büyük olan siparişlerin ortalaması nedir?
#########################################
df.head()
df.loc[(df["size"]<3) & (df["total_bill"]>10 )]

#########################################
# Görev 22: total_bill_tip_sum adında yeni bir değişken oluşturun. Her bir müşterinin ödediği totalbill ve tip in toplamını versin.
#########################################

df["total_bill_tip_sum"]=df["total_bill"]+df["tip"] 


#########################################
# Görev 23: total_bill_tip_sum değişkenine göre büyükten küçüğe sıralayınız ve ilk 30 kişiyi yeni bir dataframe'e atayınız.
########################################)
df["new"]=df.sort_values(by="total_bill_tip_sum",ascending=False).head(30)

