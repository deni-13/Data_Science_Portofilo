#  A list of lists is given:

# SPL_Patrons = [
# ['Kim Tremblay', 134, True],
# ['Emily Wilson', 42, False],
# ['Jessica Smith', 215, True],
# ['Alex Roy', 151, True],
# ['Sarah Khan', 105, False],
# ['Samuel Lee', 220, True],
# ['William Brown', 24, False],
# ['Ayesha Qureshi', 199, True],
# ['David Martin', 56, True],
# ['Ajeet Patel',69, False]
# ]
# Each sublist contains three pieces of information about the library patrons at Saskatoon Public Library (SPL) - patron's name, the number of books they have borrowed throughout the last year, and a Boolean value indicating whether they are under 20.
#%%


SPL_Patrons = [
['Kim Tremblay', 134, True],
['Emily Wilson', 42, False],
['Jessica Smith', 215, True],
['Alex Roy', 151, True],
['Sarah Khan', 105, False],
['Samuel Lee', 220, True],
['William Brown', 24, False],
['Ayesha Qureshi', 199, True],
['David Martin', 56, True],
['Ajeet Patel',69, False]
]
# (a)) Use a single list comprehension to create a list of the patron names who borrowed more than 100 books last year.
#%%


g=[i[0] for i in SPL_Patrons if i[1]>100]
g



#%%
# (b) Use a single list comprehension to create a list of the patron names who are not under 20.



young=[i[0]  for i in SPL_Patrons if i[2]==False]
young
#%%
# (c) Suppose that a patron saves on average $11.95 by borrowing a book instead of buying it. Use a single list comprehension to create a list of the amount saved for each patron.
money=[j[1]*11.95  for  j in SPL_Patrons ]
money


#%%
# (d) Use a single list comprehension to create a list of lists where each sublist consists of a patron's name and the total amount he/she saved last year as in part (c)), but only include those patrons who are under 20.



names_and_saved_amount = [[i[0], i[1]*11.95] for i in SPL_Patrons if i[2]==True]
