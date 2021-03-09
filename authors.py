
#Before inserting a string: it must start with a space and end with no spaces or commas.
old_authors = " "

# sometimes the authors may be distinguished by & or and instead of , 
old_authors = old_authors.replace(' &', ',')
old_authors = old_authors.replace(' and', ',')

# splitting all the names
name_list = old_authors.split(',')
print(name_list)

# now to add the names back together

new_names = []
stop = len(name_list) - 1
x = range(0, stop, 2)

for i in x:
    first_name = i + 1
    full_name = (name_list[first_name] + name_list[i]).lstrip()
    new_names.append(full_name)
    

print(f" These are the new names: {new_names}")

result = ', '.join(str(i) for i in new_names)
print(result)
#it could end with 'and ' for the last name...