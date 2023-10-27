

#%%# Görev6:  embarked değişkeninintipinikontrolediniz. Tipinicategory olarakdeğiştirinizvetekrarkontrolediniz

import seaborn as sns
df = sns.load_dataset("titanic")

# df["embarked"].info()  #daha detayli
# print("****")
# print(df["embarked"].value_counts()) #icindeki degiskenler


print(df.dtypes["embarked"])  #tipini goruntuleme ---1

#%%

df["embarked"]=df["embarked"].astype("category")

df.dtypes["embarked"]

df.info() #cevrildi 


# Görev7:  embarked değeriC olanlarıntümbilgelerinigösteriniz

df[df["embarked"]=="C"]

#%%Görev8:  embarked değeriS olmayanlarıntümbilgelerinigösteriniz.

df[df["embarked"]!="S"]

#%%# Görev9: Yaşı30 dan küçükvekadınolanyolcularıntümbilgilerinigösteriniz

df[(df["age"]<30) & (df["sex"]=="female")]

#%%

#Görev10:  Fare'i500'den büyükveyayaşı70 den büyükyolcularınbilgilerinigösteriniz
df[(df["fare"]>500) | (df["age"]>70)]


# %%# Görev 11:  Her birdeğişkendekiboşdeğerlerintoplamını bulunuz

df.isnull().sum()
#%%
# Görev 12:  who değişkeninidataframe’den çıkarınız.

df=df.drop("who",axis=1)
df 
#truncated oldu

#%% # Görev13:  deck değikenindekiboşdeğerlerideck değişkeninençoktekraredendeğeri(mode) ile doldurunuz.
df["deck"].head(40)

#%%
mode1=df["deck"].mode()[0]
mode1


# %%
df["deck"].fillna(mode1,inplace=True )
df["deck"].head(40)

#%%# Görev14:  age değikenindekiboşdeğerleriage değişkeninmedyanıiledoldurunuz.
median=df["age"].median()
df["age"].fillna(median,inplace=True )
df["age"]

#%%# Görev15:  survived değişkenininpclassvecinsiyetdeğişkenlerikırılımınındasum, count, mean değerlerinibulunuz

df.groupby(["pclass","sex"]).agg({"survived": ["sum","count","mean"]})




# %%Görev16: 30 yaşınaltındaolanlar1, 30a eşitveüstündeolanlara0 vericekbirfonksiyonyazın
# Yazdığınızfonksiyonukullanaraktitanikverisetindeage_flagadındabirdeğişkenoluşturunuzoluşturunuz.

# res =(lambda i: i=1.30 if i<30 else i=0 for i in df["age"]) # i= yok!

res =[ 1.30 if i<30 else 0 for i in df["age"]] # i= yok!
print(res)

df["age_flag"]=res

df["age_flag"]
