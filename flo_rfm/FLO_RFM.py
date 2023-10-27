
###############################################################
# RFM ile Müşteri Segmentasyonu (Customer Segmentation with RFM)
###############################################################

###############################################################
# İş Problemi (Business Problem)
###############################################################
# FLO müşterilerini segmentlere ayırıp bu segmentlere göre pazarlama stratejileri belirlemek istiyor.
# Buna yönelik olarak müşterilerin davranışları tanımlanacak ve bu davranış öbeklenmelerine göre gruplar oluşturulacak..

###############################################################
# Veri Seti Hikayesi
###############################################################

# Veri seti son alışverişlerini 2020 - 2021 yıllarında OmniChannel(hem online hem offline alışveriş yapan) olarak yapan müşterilerin geçmiş alışveriş davranışlarından
# elde edilen bilgilerden oluşmaktadır.

# master_id: Eşsiz müşteri numarası
# order_channel : Alışveriş yapılan platforma ait hangi kanalın kullanıldığı (Android, ios, Desktop, Mobile, Offline)
# last_order_channel : En son alışverişin yapıldığı kanal
# first_order_date : Müşterinin yaptığı ilk alışveriş tarihi
# last_order_date : Müşterinin yaptığı son alışveriş tarihi
# last_order_date_online : Muşterinin online platformda yaptığı son alışveriş tarihi
# last_order_date_offline : Muşterinin offline platformda yaptığı son alışveriş tarihi
# order_num_total_ever_online : Müşterinin online platformda yaptığı toplam alışveriş sayısı
# order_num_total_ever_offline : Müşterinin offline'da yaptığı toplam alışveriş sayısı
# customer_value_total_ever_offline : Müşterinin offline alışverişlerinde ödediği toplam ücret
# customer_value_total_ever_online : Müşterinin online alışverişlerinde ödediği toplam ücret
# interested_in_categories_12 : Müşterinin son 12 ayda alışveriş yaptığı kategorilerin listesi

###############################################################
# GÖREVLER
###############################################################

# GÖREV 1: Veriyi Anlama (Data Understanding) ve Hazırlama
           # 1. flo_data_20K.csv verisini okuyunuz.

import pandas as pd
import datetime as dt
pd.set_option('display.max_columns', None)  #sutunları 
# pd.set_option('display.max_rows', None)
pd.set_option('display.float_format', lambda x: '%.3f' % x)  #sayıal  

df_=pd.read_csv("flo_data_20k.csv")
# 2. Veri setinde a. İlk 10 gözlem,
df=df_.copy()
df.head(10)

# b. Değişken isimleri,

df.info()

# c. Betimsel istatistik,
df.describe().T

# d. Boş değer,
df.isnull().sum()
# e. Değişken tipleri, incelemesi yapınız.

df.dtypes
# 3. Omnichannel müşterilerin hem online'dan hemde offline platformlardan alışveriş yaptığını ifade etmektedir. Herbir müşterinin toplam
# alışveriş sayısı ve harcaması için yeni değişkenler oluşturun.
df["omnichannel"] = df["order_num_total_ever_online"] + df["order_num_total_ever_offline"]
df["omnichannel_total_pr"] = df["customer_value_total_ever_offline"]+df["customer_value_total_ever_online"]
df[["omnichannel","omnichannel_total_pr"]]


# 4. Değişken tiplerini inceleyiniz. Tarih ifade eden değişkenlerin tipini date'e çeviriniz.
for i in df.columns:
    if "date" in i:
        print(i)
        #df[i].astype("datetime") :D
        df[i]= pd.to_datetime(df[i])

df.dtypes
df.head()
# 5. Alışveriş kanallarındaki müşteri sayısının, ortalama alınan ürün sayısının ve ortalama harcamaların dağılımına bakınız.
df.groupby("order_channel").agg({"master_id":"count","omnichannel": "mean","omnichannel_total_pr":"mean"})

# 6. En fazla kazancı getiren ilk 10 müşteriyi sıralayınız.

df.groupby("master_id").agg({"omnichannel_total_pr":"sum"}).sort_values("omnichannel_total_pr", ascending=False).head(10)

# 7. En fazla siparişi veren ilk 10 müşteriyi sıralayınız.
df.groupby("master_id").agg({"omnichannel":"sum"}).sort_values("omnichannel", ascending=False).head(10)

# 8. Veri ön hazırlık sürecini fonksiyonlaştırınız.

def rfm_(df,head=10):
    df["total_price"]=df["omnichannel"]*df["omnichannel_total_pr"]
    df=df.dropna()
    return df.head()

# GÖREV 2: RFM Metriklerinin Hesaplanması
today=df["last_order_date"].max()  + dt.timedelta(days=2)
today
df.head()

rfm = df.groupby("master_id").agg({"last_order_date": lambda x: (today - x.max()).days,
              "omnichannel": lambda x: x,
              "omnichannel_total_pr": lambda x: x.sum()})



# GÖREV 3: RF ve RFM Skorlarının Hesaplanması
rfm.columns=["recency","frequency","monetary"]

rfm.head()
# GÖREV 4: RF Skorlarının Segment Olarak Tanımlanmasi

rfm["recency_score"] = pd.qcut(rfm['recency'], 5, labels=[5, 4, 3, 2, 1])
rfm["frequency_score"] = pd.qcut(rfm["frequency"].rank(method="first"), 5, labels=[1, 2, 3, 4, 5])
rfm["monetary_score"] = pd.qcut(rfm['monetary'], 5, labels=[1, 2, 3, 4, 5])



rfm.head()

# cltv_df skorları kategorik değere dönüştürülüp df'e eklendi
rfm["RF_SCORE"] = (rfm['recency_score'].astype(str) +
                    rfm['frequency_score'].astype(str))
rfm.head(3)
# SEGMENTLERIN ISIMLENDIRILMESI
seg_map = {
    r'[1-2][1-2]': 'hibernating',
    r'[1-2][3-4]': 'at_risk',
    r'[1-2]5': 'cant_loose',
    r'3[1-2]': 'about_to_sleep',
    r'33': 'need_attention',
    r'[3-4][4-5]': 'loyal_customers',
    r'41': 'promising',
    r'51': 'new_customers',
    r'[4-5][2-3]': 'potential_loyalists',
    r'5[4-5]': 'champions'
}

rfm['segment'] = rfm['RF_SCORE'].replace(seg_map, regex=True)



# GÖREV 5: Aksiyon zamanı!
           # 1. Segmentlerin recency, frequnecy ve monetary ortalamalarını inceleyiniz.

rfm[["recency","frequency","monetary","segment"]].groupby("segment").agg("mean")
           # 2. RFM analizi yardımı ile 2 case için ilgili profildeki müşterileri bulun ve müşteri id'lerini csv ye kaydediniz.
                   # a. FLO bünyesine yeni bir kadın ayakkabı markası dahil ediyor. Dahil ettiği markanın ürün fiyatları genel müşteri tercihlerinin üstünde. Bu nedenle markanın
                   # tanıtımı ve ürün satışları için ilgilenecek profildeki müşterilerle özel olarak iletişime geçeilmek isteniliyor. Sadık müşterilerinden(champions,loyal_customers),
                   # ortalama 250 TL üzeri ve kadın kategorisinden alışveriş yapan kişiler özel olarak iletişim kuralacak müşteriler. Bu müşterilerin id numaralarını csv dosyasına
                   # yeni_marka_hedef_müşteri_id.cvs olarak kaydediniz.
#%%
#kadin + musteri id 

target = rfm[((rfm['segment'] == 'champions') | (rfm['segment'] == 'loyal_customers'))]
spent=target.groupby("master_id")["monetary"].mean().reset_index()
spent.head()

#%%
special=spent[spent["monetary"]>250]
special

kadin=df[df["interested_in_categories_12"].str.contains("KADIN")]
target=special.merge(kadin,on="master_id")
target[["master_id"]].to_csv("yeni_marka_hedef_müşteri_id", index=False)
#%%
# b. Erkek ve Çoçuk ürünlerinde %40'a yakın indirim planlanmaktadır. Bu indirimle ilgili kategorilerle ilgilenen geçmişte iyi müşteri olan ama uzun süredir #recney dusuk : cant lose them
# alışveriş yapmayan kaybedilmemesi gereken müşteriler, uykuda olanlar ve yeni gelen müşteriler özel olarak hedef alınmak isteniliyor. Uygun profildeki müşterilerin id'lerini csv dosyasına indirim_hedef_müşteri_ids.csv
# olarak kaydediniz. !!!
df["interested_in_categories_12"]  #kategori isimleri
#%%
target2 = rfm[(rfm['segment'] == "cant_loose") | (rfm['segment'] == "about_to_sleep") | (rfm['segment'] == "new_customers")]
erkekvcocuk=df[(df["interested_in_categories_12"].str.contains("ERKEK")) &  (df["interested_in_categories_12"].str.contains("COCUK")) ]


target2=target2.merge(erkekvcocuk,on="master_id")
target2.head()
#%%
# GÖREV 6: Tüm süreci fonksiyonlaştırınız.
def create_rfm(dataframe, csv=False):

    # VERIYI HAZIRLAMA
    omnichannel=df[""]
    dataframe["total_price"]=dataframe["omnichannel"]*dataframe["omnichannel_total_pr"]
    dataframe.dropna(inplace=True)

    # RFM METRIKLERININ HESAPLANMASI
    today_date = dt.datetime(2011, 12, 11)
    rfm = dataframe.groupby('Customer ID').agg({'InvoiceDate': lambda date: (today_date - date.max()).days,
                                                'omnichannel': lambda num: num,
                                                "total_price": lambda price: price.sum()})
    rfm.columns = ['recency', 'frequency', "monetary"]
    rfm = rfm[(rfm['monetary'] > 0)]

    # RFM SKORLARININ HESAPLANMASI
    rfm["recency_score"] = pd.qcut(rfm['recency'], 5, labels=[5, 4, 3, 2, 1])
    rfm["frequency_score"] = pd.qcut(rfm["frequency"].rank(method="first"), 5, labels=[1, 2, 3, 4, 5])
    rfm["monetary_score"] = pd.qcut(rfm['monetary'], 5, labels=[1, 2, 3, 4, 5])

    # cltv_df skorları kategorik değere dönüştürülüp df'e eklendi
    rfm["RFM_SCORE"] = (rfm['recency_score'].astype(str) +
                        rfm['frequency_score'].astype(str))


    # SEGMENTLERIN ISIMLENDIRILMESI
    seg_map = {
        r'[1-2][1-2]': 'hibernating',
        r'[1-2][3-4]': 'at_risk',
        
        
        r'[1-2]5': 'cant_loose',
        r'3[1-2]': 'about_to_sleep',
        r'33': 'need_attention',
        r'[3-4][4-5]': 'loyal_customers',
        r'41': 'promising',
        r'51': 'new_customers',
        r'[4-5][2-3]': 'potential_loyalists',
        r'5[4-5]': 'champions'
    }

    rfm['segment'] = rfm['RFM_SCORE'].replace(seg_map, regex=True)
    rfm = rfm[["recency", "frequency", "monetary", "segment"]]
    if csv:
        rfm.to_csv("rfm.csv")

    return rfm

df = df_.copy()

rfm_new = create_rfm(df, csv=True)
