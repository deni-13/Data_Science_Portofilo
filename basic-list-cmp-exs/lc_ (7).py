'''
 Get the index and the value as a tuple for items in the list ["hi", 4, 8.99, 'apple', ('t,b','n')].  Result would look like [(index, value), (index, value)]
 '''
#%%
items = ["hi", 4, 8.99, 'apple', ('t,b','n')]

res=[(idx,j) for idx,j in enumerate(items)]
res

#%%
print(list((i, items[i]) for i in range(len(items))))

