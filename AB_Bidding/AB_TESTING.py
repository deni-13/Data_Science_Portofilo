#####################################################
# AB Testi ile BiddingYöntemlerinin Dönüşümünün Karşılaştırılması
#####################################################

#####################################################
# İş Problemi
#####################################################

# Facebook kısa süre önce mevcut "maximumbidding" adı verilen teklif verme türüne alternatif
# olarak yeni bir teklif türü olan "average bidding"’i tanıttı. Müşterilerimizden biri olan bombabomba.com,
# bu yeni özelliği test etmeye karar verdi veaveragebidding'in maximumbidding'den daha fazla dönüşüm
# getirip getirmediğini anlamak için bir A/B testi yapmak istiyor.A/B testi 1 aydır devam ediyor ve
# bombabomba.com şimdi sizden bu A/B testinin sonuçlarını analiz etmenizi bekliyor.Bombabomba.com için
# nihai başarı ölçütü Purchase'dır. Bu nedenle, istatistiksel testler için Purchasemetriğine odaklanılmalıdır.




#####################################################
# Veri Seti Hikayesi
#####################################################

# Bir firmanın web site bilgilerini içeren bu veri setinde kullanıcıların gördükleri ve tıkladıkları
# reklam sayıları gibi bilgilerin yanı sıra buradan gelen kazanç bilgileri yer almaktadır.Kontrol ve Test
# grubu olmak üzere iki ayrı veri seti vardır. Bu veri setleriab_testing.xlsxexcel’ininayrı sayfalarında yer
# almaktadır. Kontrol grubuna Maximum Bidding, test grubuna AverageBiddinguygulanmıştır.

# impression: Reklam görüntüleme sayısı
# Click: Görüntülenen reklama tıklama sayısı
# Purchase: Tıklanan reklamlar sonrası satın alınan ürün sayısı
# Earning: Satın alınan ürünler sonrası elde edilen kazanç



#####################################################
# Proje Görevleri
#####################################################

######################################################
# AB Testing (Bağımsız İki Örneklem T Testi)
######################################################

# 1. Hipotezleri Kur
# 2. Varsayım Kontrolü
#   - 1. Normallik Varsayımı (shapiro)
#   - 2. Varyans Homojenliği (levene)
# 3. Hipotezin Uygulanması
#   - 1. Varsayımlar sağlanıyorsa bağımsız iki örneklem t testi
#   - 2. Varsayımlar sağlanmıyorsa mannwhitneyu testi
# 4. p-value değerine göre sonuçları yorumla
# Not:
# - Normallik sağlanmıyorsa direkt 2 numara. Varyans homojenliği sağlanmıyorsa 1 numaraya arguman girilir.
# - Normallik incelemesi öncesi aykırı değer incelemesi ve düzeltmesi yapmak faydalı olabilir.

import itertools
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# !pip install statsmodels
import statsmodels.stats.api as sms
from scipy.stats import ttest_1samp, shapiro, levene, ttest_ind, mannwhitneyu, \
    pearsonr, spearmanr, kendalltau, f_oneway, kruskal
from statsmodels.stats.proportion import proportions_ztest

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 10)
pd.set_option('display.float_format', lambda x: '%.5f' % x)


#####################################################
# Görev 1:  Veriyi Hazırlama ve Analiz Etme
#####################################################

# Adım 1:  ab_testing_data.xlsx adlı kontrol ve test grubu verilerinden oluşan veri setini okutunuz. Kontrol ve test grubu verilerini ayrı değişkenlere atayınız.
control=pd.read_excel("ab_testing.xlsx",sheet_name="Control Group")
test=pd.read_excel("ab_testing.xlsx",sheet_name="Test Group")

# Adım 2: Kontrol ve test grubu verilerini analiz ediniz.
def data_analyse(data,head=5):
    print(data.describe().head())
    print("***************************")
    #shape
    print(data.shape)
    print("***************************")
    #data info
    print(data.info())
    print("***************valuecounts************")
    #value counts
    print(data.value_counts().head())
    print("*********na***********")
    print(data.isnull().sum())
    
data_analyse(control)



data_analyse(test)


control["group"]="control"
test["group"]="test"

    # Adım 3: Analiz işleminden sonra concat metodunu kullanarak kontrol ve test grubu verilerini birleştiriniz.

df = pd.concat([control, test], axis=0, ignore_index=False)
df.head()
df.tail()

#####################################################
# Görev 2:  A/B Testinin Hipotezinin Tanımlanması
#####################################################

# Adım 1: Hipotezi tanımlayınız.

# H0 : M1 = M2
# H1 : M1!= M2
#hipotez cümlesi : yapılan degisiklik sonrası kazanca noldu?

# Adım 2: Kontrol ve test grubu için purchase(kazanç) ortalamalarını analiz ediniz

df.groupby("group")["Purchase"].mean()
#####################################################
# GÖREV 3: Hipotez Testinin Gerçekleştirilmesi
#####################################################

######################################################
# AB Testing (Bağımsız İki Örneklem T Testi)
######################################################

#shapiro normal dagilim testidir
test_stat, pvalue = shapiro(df.loc[df["group"] == "control", "Purchase"])  # NORMAL DAGILIMa baktım H0 DEVAM VARYANSTAN DEVAM
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))
test_stat, pvalue = shapiro(df.loc[df["group"] == "test", "Purchase"])  # NORMAL DAGILIMa baktım  H0 DEVAM!!! VARYANSTAN DEVAM
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

# Adım 1: Hipotez testi yapılmadan önce varsayım kontrollerini yapınız.Bunlar Normallik Varsayımı ve Varyans Homojenliğidir.
#VARYANSA BAKALIM ..... LEVENE
# Kontrol ve test grubunun normallik varsayımına uyup uymadığını Purchase değişkeni üzerinden ayrı ayrı test ediniz

test_stat, pvalue = levene(df.loc[df["group"] == "control", "Purchase"],
                           df.loc[df["group"] == "test", "Purchase"])
                            #levene ile varyans control 
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))


# Adım 2: Normallik Varsayımı ve Varyans Homojenliği sonuçlarına göre uygun testi seçiniz

#HO RED!!! EVET,BİR DEGİSİKLİK VAR

# Adım 3: Test sonucunda elde edilen p_value değerini göz önünde bulundurarak kontrol ve test grubu satın alma
# ortalamaları arasında istatistiki olarak anlamlı bir fark olup olmadığını yorumlayınız.
#----------------------------------------------------------------------------------------------------------------------------------
# test_stat, pvalue = mannwhitneyu(df.loc[df["group"] == "control", "Purchase"],
#                            df.loc[df["group"] == "test", "Purchase"])
# print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))  ----|> BOYLE BİR SEY YOK  EGER NORMALUN P VAL 005 DEN KUCUK OLSAYDI 
#T TEST UYGULA


test_stat, pvalue = ttest_ind(df.loc[df["group"] == "control", "Purchase"],
                           df.loc[df["group"] == "test", "Purchase"],
                           equal_var=True)
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))



#H0 KABUL COKTAN GECTİ 005 'İ

##############################################################
# GÖREV 4 : Sonuçların Analizi
##############################################################

# Adım 1: Hangi testi kullandınız, sebeplerini belirtiniz.

# SHAPİRO
#LEVENE
#TT TESTİ 


# Adım 2: Elde ettiğiniz test sonuçlarına göre müşteriye tavsiyede bulununuz.
#YANİ BU PROJE İÇİN DE KAZANILAN PARA TASARIMSAL OLARAK DEGİSİKLİK YAPINCA DEGİSMEMİŞ 
# HO reddedilemez. Kontrol ve test grubu satın alma ortalamaları arasında istatistiksel olarak anlamlı farklılık yoktur.
