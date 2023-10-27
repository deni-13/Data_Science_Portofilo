import seaborn as sns
df=sns.load_dataset("car_crashes")


full_col=df.columns

og_list=["abbrev","no_previous"]



getir=[i for i in full_col if i not in og_list]


df[getir]
