
#%%


#  Write a function named odd_or_zero which takes one parameter, a number, and returns that number if it is odd or returns 0 if the number is even. Then using a list comprehension which iterates over a_list and calls your odd or zero function for each value, print a list like the following:
#[ 1, 0, 3, 0, 5, 0, 7, 0, 9, 0 ]


a_list = list(range(1, 11))


[0  if i%2==0 else i for i in a_list]
#%%alt
def zero(num):
    if num%2==0:
        num==0
    else:
        return num
    
[zero(i) for i in a_list]

#%%
# (e) Prompt the user for a number, which will be returned from input as a string data type. Strings can be iterated over like lists, such that the loop repeats for each character in the string. Using a list comprehension which iterates over the user-entered string and whose output expression accesses values from a_dictionary, print a list of the text form of each digit from the user-entered string, e.g.,
# Enter a number: 195
# [ 'one', 'nine', 'five' ]


string=str(input())

print(b)
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

[a_dictionary[int(i)] for i in string]
