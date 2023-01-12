print("Problem: While purchasing certain items, a discount of 10% is offered if the quantity purchased is more than 1000. If quantity and price per item are input through the keyboard, write a program to calculate the total expenses.")

print("Solution:")

qty = int(input("Enter the value of quantity:"))
price = float(int(input("Enter the value of price:")))

if qty >1000:
    dis=10
else:
    dis=0

totexp = qty * price - qty * price * dis / 100
print("Total expenses = SGD" + str(totexp))
