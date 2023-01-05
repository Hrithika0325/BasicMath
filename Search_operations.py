quantity= input('Enter quantity of numbers:')
print("quantity is equal to", quantity)
numbers= input('Enter the values:')
print("numbers are", numbers)
search= input('Enter the number to search:')
print("Number to search is", search)

if search in numbers:
    print("Found")
else:
   print("Not in") 