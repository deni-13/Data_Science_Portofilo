


# # Write a program that removes duplicates from the list (the order must be kept) and print the list to the console.

#%%



items = [1, 5, 3, 2, 2, 4, 2, 4]

list(set([i for i in items ]))
#%%

items = [1, 5, 3, 2, 2, 4, 2, 4]

unique_items = []
[unique_items.append(item) for item in items if item not in unique_items]

print(unique_items)
