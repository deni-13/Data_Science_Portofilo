#  Add % in front and end of every single word in a given string str: "Fall is Awesome in Alabama" only using list comprehensions.

# Desired Output

# ['%Fall%','%is%','%Awesome%','%in%','%Alabama%']
#%%
s="Fall is Awesome in Alabama"
lst=["%"+i+"%" for i in s.split()]
lst