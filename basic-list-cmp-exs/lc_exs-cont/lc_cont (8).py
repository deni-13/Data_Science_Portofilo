# A list of lists is given:

# prairie_pirates = [
# ['Tractor Jack', 1000, True],
# ['Plowshare Pete', 950, False],
# ['Prairie Lily', 245, True],
# ['Red River Rosie', 350, True],
# ['Mad Athabasca McArthur', 842, False],
# ['Assiniboine Sally', 620, True],
# ['Thresher Tom', 150, True],
# ['Cranky Canola Carl', 499, False]
# ]
# Each sublist contains three pieces of information on one famous prairie pirate- their pirate name (pirates can have secret identities too!), the number of sacks of assorted grains they have plundered from unsuspecting farmers in the last year, and a Boolean value indicating whether they like parrots.

# (a) Use a single list comprehension to create a list of the pirate names who plundered more than 400 sacks of assorted grains.

#%%
prairie_pirates = [
['Tractor Jack', 1000, True],
['Plowshare Pete', 950, False],
['Prairie Lily', 245, True],
['Red River Rosie', 350, True],
['Mad Athabasca McArthur', 842, False],
['Assiniboine Sally', 620, True],
['Thresher Tom', 150, True],
['Cranky Canola Carl', 499, False]
]


[i[0] for i in prairie_pirates if i[1]>400]

#(b) Use a single list comprehension to create a list of the pirate names who likes parrots.



likes=[i[0] for i in prairie_pirates if i[2]==True]