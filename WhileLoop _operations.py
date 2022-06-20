print("Hello World!, This is my seventh program")
print("WhileLoop operations - Playing with loops")
"""
#Login to Find average of the 3 numbers
x=int(input('Enter value of x:'))
y=int(input('Enter value of y:'))
z=int(input('Enter value of z:'))
avg=((x+y+z)/3)
print("average of x,y,z is:",avg)
"""

"""
#Login to Find nth term of AP and sum of n terms
a=int(input('Enter first value of AP:'))
b=int(input('Enter second value of AP:'))
c=int(input('Enter third value of AP:'))
n=int(input('Enter term of AP you want:'))
d=b-a
an=a+(n-1)*d
sum= (a+an)*n/2
print("nth term of AP is", an)
print("sum of first n terms is", sum)
"""
"""
#Logic to Print first 10 even numbers
i=2
while i<=20:
    print(i);
    i=i+2
"""
"""
#Logic to Print first 10 odd numbers
i=1
while i<=20:
    print(i);
    i=i+2
"""
a=int(input('Enter value of a:'))
b=int(input('Enter value of b:'))
n=int(input('Enter number of terms you want:'))
d=b-a

print("First number of series is" , a)
print("Second number of series is" ,b)
series=2
while series<n:
       print("Next number of the series is",b+d)
       b=b+d
       series = series +1
          
   