
#%%gorev 6
muh_f=[]
tip_f=[]
ogrenciler=["Ali", "Veli", "Ayşe", "Talat", "Zeynep", "Ece"]
for j in range(len(ogrenciler)):
    if j<3:
        muh_f.append(ogrenciler[j])
    else:
        tip_f.append(ogrenciler[j])


for i in (enumerate(muh_f,1)):  #1den basla
    print("Muh Fak "+ str(i[0])+ "" + "."+" "+"ogrenci: "  + i[1] ) 
for i in enumerate(tip_f,1):  #1den basla
    print("Tıp Fak "+ str(i[0])+ "" + "."+" "+"ogrenci: "  + i[1] ) 



# %% gorev 7

ders_kodu=["CMP1005","PSY1001", "HUK1005", "SEN2204"]
kredi = [3,4,2,4]
kontenjan=[30,75,150,25]
#farkli listeleri birlesitrmenin akternatif 
for i,j,k in zip(kredi,ders_kodu,kontenjan):
    print(f"Kredisi {i} olan {j} kodlu dersin kontenjanı {k} kisidir.")

#%%gorev 8

kume1 =set(["data", "python"])
kume2 =set(["data", "function", "qcut", "lambda", "python", "miuul"])


if kume2.issubset(kume1):
    print(kume1.intersection(kume2))
else:
    print(kume2.difference(kume1))

#alternating way 
if kume1.issuperset(kume2):
    print(kume1.intersection(kume2))
else:
    print(kume2.difference(kume1))


