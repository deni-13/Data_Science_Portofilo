# Write a program which extracts exactly ,
# the first four words as a list.
# Standardize each word,
# i.e. replace uppercase letters with lowercase. 
# Present the result in a list and print to the console as shown below.

#%%
text = 'Python is a very popular programming language'.lower()
w=text.split(" ")
l=[]
for i in range(4):
    l.append(w[i])
print(l)
#%%

#alt

text = 'Python is a very popular programming language'
 
words = text.split(' ')
result = []
for idx, word in enumerate(words):
    if idx < 4:
        result.append(word.lower())
print(result)