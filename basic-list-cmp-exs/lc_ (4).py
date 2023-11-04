'''Find all of the words in a string that are less than 4 letters'''
#%%
sentence = 'On a summer day somner smith went simming in the sun and his red skin stung'

[i for i in sentence.split() if len(i)<=4]
