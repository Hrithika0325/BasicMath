print("Hello World!, This is my sixth program")
print("Condition operations - Playing with conditions")

age=int(input('Enter age:'))
if (age >2 and age <18):
    print("Person is youngster")
elif (age >18 and age <60):
    print("Person is adult")
elif (age >=60 and age <100):
    print("Person is Senior Citizen")
elif age ==100:
    print("Person is Perfect Citizen")
else:
    print("Person is toddler")


