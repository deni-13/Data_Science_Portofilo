# 14 Consider a list of full names formatted "Firstname Lastname", like ["Jules Verne", "Alexandre Dumas", "Maurice Druon"].
#%%

# #  Consider a list of full names formatted "Firstname Lastname", like ["Jules Verne", "Alexandre Dumas", "Maurice Druon"
# Write a list comprehension that produces a list with
# the full names in the format "Lastname, Firstname". 
# he resulting list should look like

# ['Verne, Jules', 'Dumas, Alexandre', 'Druon, Maurice']


l=["Jules Verne", "Alexandre Dumas", "Maurice Druon"]

[i.split()[1] +" " + i.split()[0] for i in l]
#bosluga gore split