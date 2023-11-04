# 3 Write a list comprehension that builds a list containing only the names with at least 8 characters.

# Input
#%%
avengers = ["Iron Man", "Captain America", "Thor", "The Incredible Hulk", "Bla avengers ck Widow", "Hawkeye"]


[av for av in avengers if len(av)>=8]
