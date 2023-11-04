#https://www.tutorialsandyou.com/python/python-list-comprehension-practice-exercises-and-problems-101.html
#%%
# 1 Consider the following list and dictionary in your code:

a_list = list(range(1, 11))
a_dictionary = {
1 : 'one',
2 : 'two',
3 : 'three',
4 : 'four',
5 : 'five',
6 : 'six',
7 : 'seven',
8 : 'eight',
9 : 'nine',
10 : 'ten'}


#(a) Use a list comprehension that iterates over a_list, prints a list composed of each value in a_list multiplied by 10.


[i*10 for i in a_list]

#%%

#(b) Use a list comprehension that iterates over a_list, prints a list composed of odd numbers from 1 to 9.

[i for i in a_list if i <10 and i%2==1]
#%%
#) Using a list comprehension which iterates over a_list and whose output expression accesses a value from a dictionary, print a list composed of the text form of each even number from 2 to 10, e.g.,[ 'two', 'four', 'six', 'eight', 'ten' ]

a_dictionary = {
1 : 'one',
2 : 'two',
3 : 'three',
4 : 'four',
5 : 'five',
6 : 'six',
7 : 'seven',
8 : 'eight',
9 : 'nine',
10 : 'ten'}


[j for i,j in a_dictionary.items() if i%2==0 ]