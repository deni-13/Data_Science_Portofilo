#%%Write a program that returns a list of values above the given threshold = 0.5 from the following list:

probabilities = [0.21, 0.91, 0.34, 0.55, 0.76, 0.02]

[i for i in probabilities if i >0.5]


#%%
probabilities = [0.21, 0.91, 0.34, 0.55, 0.76, 0.02]
result = []
 
for prob in probabilities:
    if prob > 0.5:
        result.append(prob)
        
print(result)