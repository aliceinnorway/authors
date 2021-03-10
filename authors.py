#Before inserting a string it must end with no spaces or commas.
old_authors = ""

# sometimes the authors may be distinguished by & or and instead of , 
old_authors = old_authors.replace(' &', ',')
old_authors = old_authors.replace(' and', ',')
old_authors = old_authors.replace('Kjeld S.', 'Kjeld Steenbjerg') #This is because Wix is only recognising Kjeld as Kjeld Steenbjerg

# splitting all the names
name_list = old_authors.split(',')

# add a space before the first surname
name_list[0] = ' ' + name_list[0]

# add 'and' for the last name
name_list[-2] = 'and ' + name_list[-2]

# now to add the names back together
new_names = []
stop = len(name_list) - 1
x = range(0, stop, 2)

for i in x:
    first_name = i + 1
    # this line below is where its switches the names
    full_name = (name_list[first_name] + name_list[i]).lstrip()
    new_names.append(full_name)
    
result = ', '.join(str(i) for i in new_names)
print(result)


