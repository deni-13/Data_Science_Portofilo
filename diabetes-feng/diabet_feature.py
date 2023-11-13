import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
# !pip install missingno
import missingno as msno
from datetime import date
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import LocalOutlierFactor
from sklearn.preprocessing import MinMaxScaler, LabelEncoder, StandardScaler, RobustScaler

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.float_format', lambda x: '%.3f' % x)
pd.set_option('display.width', 500)


#genel resim

def load():
    data = pd.read_csv("diabetes.csv")
    return data


df=load()
df.head()
df.shape
df.info()
df.value_counts().head()
# =============================================================================
# ---  ------                    --------------  -----  
#  0   Pregnancies               768 non-null    int64  
#  1   Glucose                   768 non-null    int64  
#  2   BloodPressure             768 non-null    int64  
#  3   SkinThickness             768 non-null    int64  
#  4   Insulin                   768 non-null    int64  
#  5   BMI                       768 non-null    float64
#  6   DiabetesPedigreeFunction  768 non-null    float64
#  7   Age                       768 non-null    int64  
#  8   Outcome                   768 non-null    int64  
# dtypes: float64(2), int64(7)
# =============================================================================
#outcome : categorik

#%%2-numeric and cats determining
def grab_col_names(dataframe, cat_th=10, car_th=20):

    # cat_cols, cat_but_car
    cats = [col for col in dataframe.columns if dataframe[col].dtypes == "O"]
    num_but_cat = [col for col in dataframe.columns if dataframe[col].nunique() < cat_th and dataframe[col].dtypes != "O"]
    cat_but_car = [col for col in dataframe.columns if dataframe[col].nunique() > car_th and dataframe[col].dtypes == "O"]
    cats = cats + num_but_cat
    cats = [col for col in cats if col not in cat_but_car]
    
    # num_cols
    nums = [col for col in dataframe.columns if dataframe[col].dtypes != "O"]
    nums = [col for col in nums if col not in num_but_cat]
    
    print(f"Observations: {dataframe.shape[0]}")
    print(f"Variables: {dataframe.shape[1]}")
    print(f'cat_cols: {len(cats)}')
    print(f'num_cols: {len(nums)}')
    print(f'cat_but_car: {len(cat_but_car)}')
    print(f'num_but_cat: {len(num_but_cat)}')
    return cats, nums, cat_but_car

cats, nums, cat_but_car = grab_col_names(df)
#hedef degisken analizi

df.groupby("Outcome")["Glucose","BMI","BloodPressure"].mean()



#%% target vs nums

def cat_mean(dataframe, nums,target):
    print(df.groupby(target)[nums].mean())
    


def target_summary_with_num(dataframe, target, nums):
    print(dataframe.groupby(target).agg({nums: "mean"}), end = "\n\n\n")
    
for col in nums:
    target_summary_with_num(df, "Outcome", col)
    
    
#cat_mean(df,"Glucose","Outcome")  


    
#%% 5- for outliers

def outlier(data,cols,q=0.25,qq=0.75):
    q1=data[cols].quantile(0.25)
    q3=data[cols].quantile(qq)
    iqr=q3-q1
    up=q3+1.5*iqr
    low=q1-1.5*iqr
    
    
    return low,up


# print("low,Up")
# print(outlier(df, nums))

outlier(df,"Glucose")
outlier(df,"Insulin")  #0 olan degerler var



low, up = outlier(df,"Glucose")

df[(df["Glucose"] < low) | (df["Glucose"] > up)].head()

len(df[(df["Glucose"] < low) | (df["Glucose"] > up)])

df[(df["Insulin"] < low) | (df["Insulin"] > up)].head()


len(df[(df["Insulin"] < low) | (df["Insulin"] > up)])


df[(df["Insulin"] < low) | (df["Insulin"] > up)].index

   #%% 6- outlier control missing ratio
def check_outlier(data,cols):
    low,up=outlier(data, cols)
    if data[(data[cols]<low) | (data[cols]>up)].any(axis=None):
        return True
    return False
check_outlier(df,"Insulin")        

def missin_vals(data,na_name=False):
    na_columns = [col for col in data.columns if data[col].isnull().sum() > 0]

    n_miss = data[na_columns].isnull().sum().sort_values(ascending=False)
    ratio = (data[na_columns].isnull().sum() / data.shape[0] * 100).sort_values(ascending=False)
    missing_df = pd.concat([n_miss, np.round(ratio, 2)], axis=1, keys=['n_miss', 'ratio'])
    print(missing_df, end="\n")

    if na_name:
        return na_columns
    
    #there s no null values 
    
missin_vals(df,True)





#%% 7-corr 

msno.bar(df)  #missing no bar chart
plt.show()
msno.matrix(df)
plt.show()

msno.heatmap(df)
plt.show()

#%% eksik degr doldurma 0---|> NaN
zero_columns = [col for col in df.columns if (df[col].min() == 0 and col not in ["Pregnancies", "Outcome"])]
zero_columns


for col in zero_columns:
    df[col] = np.where(df[col] == 0, np.nan, df[col])  #NaN
    
    
df.head()

df.isnull().sum()

#0 ::::|> nan

#%% % ne kadar NaN
def missing_vals(dataframe, na_name=False):
    na_columns = [col for col in dataframe.columns if dataframe[col].isnull().sum() > 0]

    n_miss = dataframe[na_columns].isnull().sum().sort_values(ascending=False)
    ratio = (dataframe[na_columns].isnull().sum() / dataframe.shape[0] * 100).sort_values(ascending=False)
    missing_df = pd.concat([n_miss, np.round(ratio, 2)], axis=1, keys=['n_miss', 'ratio'])
    print(missing_df, end="\n")

    if na_name:
        return na_columns


missing_vals(df)

missing_vals(df, True)
#%%

for col in zero_columns:
   df.loc[df[col].isnull(), col] = df[col].median()
    
df1=df.copy()
df1.head()
#%%

df1.describe()  #all is filled
df1.info()
df1.head()
#%% feature extraction




# =============================================================================
# 
# Feature engineering, veri setinizdeki mevcut özelliklerin üzerine yeni özellikler oluşturarak veya mevcut özellikleri dönüştürerek daha fazla bilgi çıkarmayı içerir. Veri setinizdeki özelliklerin türüne ve veriye bağlı olarak farklı özellik mühendisliği teknikleri kullanabilirsiniz. İşte bu tür bir veri seti için örnek feature engineering adımları:
# 
# 1. Vücut Kitle İndeksi (BMI) Kategorileri:
#    - BMI değerlerini kategorilere dönüştürerek, aşırı kilolu, obez veya normal kilolu gibi kategorik bir özellik oluşturabilirsiniz. Örneğin, BMI < 18.5 için "Zayıf", 18.5 - 24.9 için "Normal", 25 - 29.9 için "Aşırı Kilolu" vb.
# 
# 2. Yaş Grupları:
#    - Yaş özelliklerini yaş gruplarına dönüştürerek, gençler, yetişkinler ve yaşlılar gibi yaş gruplarına dayalı bir özellik oluşturabilirsiniz.
# 
# 3. Diyabet Geçmişi:
#    - DiabetesPedigreeFunction değeri belirli bir eşik değerini aşıyorsa "Ailede Diyabet Geçmişi Var" gibi bir kategorik özellik oluşturabilirsiniz.
# 
# 4. Kan Basıncı Sınıfları:
#    - BloodPressure değerlerini düşük, normal ve yüksek kan basıncı kategorilerine dönüştürerek bir sınıflandırma özelliği oluşturabilirsiniz.
# 
# 5. Hamilelik Sıklığı:
#    - Pregnancies özelliğini sıfır veya sıfır olmayan hamilelikler olarak iki ayrı sınıfa ayırarak bir yeni özellik oluşturabilirsiniz.
# 
# 6. İnsülin Direnci:
#    - Insulin özelliği, normal insülin seviyelerine sahip olanlar ve insülin direnci olanlar olarak iki sınıfa ayrılabilir.
# 
# 7. Glukoz Seviyeleri:
#    - Glucose değerlerini düşük, normal ve yüksek glukoz seviyelerine sahip olanlar olarak sınıflandırabilirsiniz.
# 
# 8. Deri Kalınlığı Grupları:
#    - SkinThickness değerlerini belirli aralıklarda gruplandırarak yeni bir özellik oluşturabilirsiniz.
# 
# 9. Toplam Hamilelik Sayısı:
#    - Pregnancies özelliği ile Age özelliğini çarpıp yeni bir "Toplam Hamilelik Sayısı" özelliği oluşturabilirsiniz.
# 
# 10. İnsülin ve Glukoz Oranı:
#     - Insulin ve Glucose değerlerini birbirine oranlayarak insülin hassasiyetini yansıtan bir özellik oluşturabilirsiniz.
# 
# =============================================================================
#Pregnancies  Glucose  BloodPressure  SkinThickness  Insulin     BMI  DiabetesPedigreeFunction     Age

#%%yas ve bmi
pd.cut(df1["Age"],3)
df1["BMI"].describe()

# [(20.94, 41.0] < (41.0, 61.0] < (61.0, 81.0]
# 0 ila 18,4 BMI: Zayıf. ...
# 18.5 ila 24.9 BMI: Normal. ...
# 25 ila 29.9 BMI: Fazla Kilolu. ...
# 30 ila 34.9 BMI: Şişman. ...
# 35 ila 44.9 BMI: Şişman. ...
# 45+ BMI: Aşırı Şişman.

# df['BMI_Degree'].value_counts()

# Fat2      200
# OverW     173
# Fat1      167
# Normal    102
# Obese      35
# Thin       15
#%% 





# BMI_Degree özelliği oluşturma
df1.loc[df1['BMI'] > 45, 'BMI_Degree'] = 'Obese'
df1.loc[(df1['BMI'] > 35) & (df1['BMI'] <= 45), 'BMI_Degree'] = 'Fat2'
df1.loc[(df1['BMI'] > 30) & (df1['BMI'] <= 35), 'BMI_Degree'] = 'Fat1'
df1.loc[(df1['BMI'] > 25) & (df1['BMI'] <= 30), 'BMI_Degree'] = 'OverW'
df1.loc[(df1['BMI'] >= 18.5) & (df1['BMI'] <= 25), 'BMI_Degree'] = 'Normal'
df1.loc[df1['BMI'] < 18.5, 'BMI_Degree'] = 'Thin'
df1.head()
#%%
# BMIVsAGE özelliği oluşturma
df1.loc[(df1['BMI_Degree'] == 'Obese') & ((df1['Age'] > 18) & (df1['Age'] <= 41)), 'BMIVsAGE'] = 'OBESEYOUNG'
df1.loc[(df1['BMI_Degree'] == 'Obese') & ((df1['Age'] > 41) & (df1['Age'] < 61)), 'BMIVsAGE'] = 'OBESEMED'
df1.loc[(df1['BMI_Degree'] == 'Obese') & (df1['Age'] >= 61), 'BMIVsAGE'] = 'OBESEOLD'

df1.loc[(df1['BMI_Degree'] == 'Fat2') & ((df1['Age'] > 18) & (df1['Age'] <=41)), 'BMIVsAGE'] = 'FAT2YOUNG'
df1.loc[(df1['BMI_Degree'] == 'Fat2') & ((df1['Age'] > 41) & (df1['Age'] < 61)), 'BMIVsAGE'] = 'FAT2MED'
df1.loc[(df1['BMI_Degree'] == 'Fat2') & (df1['Age'] >= 61), 'BMIVsAGE'] = 'FAT2OLD'

df1.loc[(df1['BMI_Degree'] == 'Fat1') & ((df1['Age'] > 18) & (df1['Age'] <= 41)), 'BMIVsAGE'] = 'FAT1YOUNG'
df1.loc[(df1['BMI_Degree'] == 'Fat1') & ((df1['Age'] > 41) & (df1['Age'] < 61)), 'BMIVsAGE'] = 'FAT1MED'
df1.loc[(df1['BMI_Degree'] == 'Fat1') & (df1['Age'] >= 61), 'BMIVsAGE'] = 'FAT1OLD'

df1.loc[(df1['BMI_Degree'] == 'OverW') & ((df1['Age'] > 18) & (df1['Age'] <= 41)), 'BMIVsAGE'] = 'OVERYOUNG'
df1.loc[(df1['BMI_Degree'] == 'OverW') & ((df1['Age'] > 41) & (df1['Age'] < 61)), 'BMIVsAGE'] = 'OVERMED'
df1.loc[(df1['BMI_Degree'] == 'OverW') & (df1['Age'] >= 61), 'BMIVsAGE'] = 'OVEROLD'

df1.loc[(df1['BMI_Degree'] == 'Normal') & ((df1['Age'] > 18) & (df1['Age'] <= 41)), 'BMIVsAGE'] = 'NORMALYOUNG'
df1.loc[(df1['BMI_Degree'] == 'Normal') & ((df1['Age'] > 41) & (df1['Age'] < 61)), 'BMIVsAGE'] = 'NORMALMED'
df1.loc[(df1['BMI_Degree'] == 'Normal') & (df1['Age'] >=61), 'BMIVsAGE'] = 'NORMALOLD'

df1.loc[(df1['BMI_Degree'] == 'Thin') & ((df1['Age'] > 18) & (df1['Age'] <= 41)), 'BMIVsAGE'] = 'THINOLD'
df1.loc[(df1['BMI_Degree'] == 'Thin') & ((df1['Age'] > 41) & (df1['Age'] < 61)), 'BMIVsAGE'] = 'THINMED'
df1.loc[(df1['BMI_Degree'] == 'Thin') & (df1['Age'] >= 61), 'BMIVsAGE'] = 'THINOLD'

df1.head()
df1.BMI_Degree.isnull().sum()

df1.BMIVsAGE.isnull().sum()

#%% DiabetesPedigreeFunction ve  glucose 
df1.DiabetesPedigreeFunction.describe()

#kategorik yapalim
df1.loc[df["DiabetesPedigreeFunction"]<df["DiabetesPedigreeFunction"].mean(),"DIABET_HISTORY"]="no"

df1.loc[df["DiabetesPedigreeFunction"]>df["DiabetesPedigreeFunction"].mean(),"DIABET_HISTORY"]="yes"
df1.head()

#insulin direnci yes or no
#%%

# Glukoz degerini kategorik değişkene çevirme
df1.Glucose.describe()
df1["NEW_GLUCOSE"] = pd.cut(x=df1["Glucose"], bins=[0, 140, 200, 300], labels=["Normal", "Prediabetes", "Diabetes"])
# count   768.000
# mean    121.656
# std      30.438
# min      44.000
# 25%      99.750
# 50%     117.000
# 75%     140.250
# max     199.000

df1["NEW_GLUCOSE"]=df1["NEW_GLUCOSE"].astype("object")
df1.info()

#%% kan basinci


df.BloodPressure.describe()

df1["BlOOD"]=pd.cut(df1["BloodPressure"],bins=[0,65,80,200],labels=["Normal","Little High","High"])

df1.info()


df1["BlOOD"]=df1["BlOOD"].astype("object")

df1.info()
#%% encoding---- !!!
#blood 3
cats,nums,cat_but_car =grab_col_names(df1)

df1["Glucose"].nunique()



# %% LABEL ENCODING
def label_encoder(dataframe, binary_col):
    labelencoder = LabelEncoder()
    dataframe[binary_col] = labelencoder.fit_transform(dataframe[binary_col])
    return dataframe

binary_col = [col for col in df1.columns if df1[col].dtypes == "object" and df1[col].nunique() == 2]

for col in binary_col:
    df1 = label_encoder(df1, col)
df1.head()
#%%
cats= [col for col in cats if col not in binary_col and col not in ["OUTCOME"]]

def one_hot_encoder(dataframe, categorical_cols, drop_first=False):
    dataframe = pd.get_dummies(dataframe, columns=categorical_cols, drop_first=drop_first)
    return dataframe

df1 = one_hot_encoder(df1, cats,drop_first=True)

df1.head()

#%% standartlastirma

ss = StandardScaler()

df1[nums] = ss.fit_transform(df1[nums])

df1.info()
#%% modelling

y = df1["Outcome_1"]
X = df1.drop(["Outcome_1"], axis=1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=17)

from sklearn.ensemble import RandomForestClassifier

rf_model = RandomForestClassifier(random_state=46).fit(X_train, y_train)
y_pred = rf_model.predict(X_test)
accuracy_score(y_pred, y_test)


def plot_importance(model, features, num=len(X), save=False):
    feature_imp = pd.DataFrame({'Value': model.feature_importances_, 'Feature': features.columns})
    plt.figure(figsize=(10, 10))
    sns.set(font_scale=1)
    sns.barplot(x="Value", y="Feature", data=feature_imp.sort_values(by="Value",
                                                                      ascending=False)[0:num])
    plt.title('Features')
    plt.tight_layout()
    plt.show()
    if save:
        plt.savefig('importances.png')



plot_importance(rf_model, X)