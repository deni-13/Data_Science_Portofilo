
#%%
#1 wowel starts with name?
students="al","jonh","mateo","ed","alice"
wowel="aeiou"
w=[]
for i in  students:
    if i[0] in wowel:
        w.append(i)
w

#%% list compr

[j for  j in students if j[0] in wowel]