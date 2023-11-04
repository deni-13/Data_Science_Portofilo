# Count the number of spaces in a string
#%%
str="istanbul is good"
# print([i.count("") for i in str if "" in i]) patladi [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]


space=[s for s in str if s==" "]
len(space)