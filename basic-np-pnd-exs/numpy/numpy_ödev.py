# Numpy Odev
#%%
import numpy as np
#%%  Soru1-> (5,5)'lik 1'lerden olusan bir matris ile ayni boyutta 0'lardan olusan matrisi birlestirin.

b=np.ones((5,5))
i=np.zeros((5,5))
c=np.vstack((b,i))
d=np.hstack((b,i))

#%% Soru2 -> 3'den 100'e kadar olan degerlerden 3'ye tam bolunebilenlerle bir array olusturun

np.arange(3,100,3)

#%%  Soru3 -> 5 tane 7 bulunan bir vektor olusturun.
np.ones(5)*7


#%% Soru4 -> 0 ile 10 arasindaki rastgele int degerler ile (3,3)'lik matris olusturun.
np.random.randint(0,10,9).reshape(3,3)



#%%  Soru5 -> 1' den 100'e kadar (10,10)'luk bir matris olusturun.

a=np.arange(1,101).reshape(10,10)


#%%  Soru6 -> Son olusturdugunuz matrisin sadece 1. satirini alin ve (2,5)'lik hale getirin.
import numpy as np
a=np.arange(1,101).reshape(10,10)
a[0,::].reshape(2,5)



#%% Soru7 -> 0 ile 1 arasindaki rastgele sayilar ile (5,5)'lik matris olusturun ve 2 satir ve sonrasini alin.

np.linspace(0,1,25).reshape(5,5)

#%%  Soru8 -> 0 ile 10 arasindaki rastgele int degerler ile (7,7)'lik matris olusturun ve 3. satira kadar alin ve 4. sitindan sonrasini alin.
import numpy as np


np.linspace(0,10,49).reshape(7,7)


#%%  Soru9 -> En son buldugunuz matrisin butun elamanlarinin toplamini, max ve min degerlerini bulun.

d=np.linspace(0,10,49).reshape(7,7)
d.max()
d.min()
d.sum()
#%%  Soru10 -> (5,5)' lik bir 0 matrisi olusturun ve elemanlarin hepsini 10 yapin.
import numpy as np


m=np.zeros(25).reshape(5,5)
for i in range(len(m)):
    m[i]=10

print(m)

#%% Soru11 -> 0 ile 10 arasini esit parcalara bolen (4,4)'lik bir matris olusturun.

son=np.linspace(0,10,16).reshape(4,4)

#%% Soru12 -> Son olusturdugunuz matrisdeki 5'den buyuk degerleri 0 yapin.
son=np.linspace(0,10,16).reshape(4,4)

for i in range(len(son)):
    
    for j in range(len(son)):
        if son[i,j]>5:
            son[i,j]=0

print(son)








