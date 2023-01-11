# Create a list of 5 names 
names = ['Anil', 'Amol', 'Aditya', 'Avi', 'Alka']
print(names)

# insert a name 'Anuj' before 'Aditya'
names.insert(2, 'Anuj')
print(names)

# append a name 'Zulu'
names.append('Zulu')
print(names)

# delete 'Avi' from the list
names.remove('Avi')
print(names)

# replace 'Anil' with 'AnilKumar'
i=names.index('Anil')
names[i] = 'AnilKumar'
print(names)

# sort all the names in the list
names.sort()
print(names)

# print reversed sorted list 
names.reverse()
print(names)