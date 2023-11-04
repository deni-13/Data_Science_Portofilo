# https://bbookman.github.io/Python-list-comprehension1/

#Find all of the numbers from 1-1000 that are divisible by 7

div7 = [n for n in range(1,1000) if n % 7 == 0] 
print(div7)