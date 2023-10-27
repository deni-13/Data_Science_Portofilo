#eda + pandas + np case---3.1

#%%

import warnings
warnings.filterwarnings("ignore")

import numpy as np
import seaborn as sns
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)



df = sns.load_dataset("titanic")
df.head()
df.shape
#%%
# Görev 2: Titanic veri setindeki kadın ve erkek yolcuların sayısını bulunuz.

f=df[df["sex"]=="female"].count()
m=df[df["sex"]=="male"].count()
f 

#%%gorev 2
df["sex"].value_counts()  # alt

#%%-----------------------
# Görev 3: Her bir sutuna ait unique değerlerin sayısını bulunuz. <-----!!
df.nunique()

#%%# .Görev4:  pclassdeğişkenininunique değerlerininsayısınıbulunuz.

d=df["pclass"].nunique()

d
#%%# alternatif 
df["pclass"].value_counts()



#%% gorev 5 # Görev5:  pclassveparch değişkenlerininunique değerlerininsayısınıbulunuz
df.columns
cols=["pclass","parch"]


df.loc[:,cols].nunique()


