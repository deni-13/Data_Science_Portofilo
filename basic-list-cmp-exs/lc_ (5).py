#%%
l=[11,22,33,44,55,66,77,88,99]


[i if i%11==0 else []  for i in l  ] 

#%%

# # Write a program that finds all two-digit numbers divisible by 11 (use a for loop). Print the result to the console as comma-separated values as shown below.



# # Expected result:



# # 11,22,33,44,55,66,77,88,99
l=[11,22,33,44,55,66,77,88,99]
res=[]
for i in l:
    if i %11==0:
        res.append(str(i))
#print(res)
print(",".join(res))

