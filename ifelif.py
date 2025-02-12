#WAP to check greater number between two using if else statement

a= int(input("Enter a\n"))
b= int(input("Enter b\n"))
c= int(input("Enter c\n"))
d= int(input("Enter d\n"))

if a>b and a>c and a>d:
 print("a is greater")
 print("a=",a)

elif b>c and b>d:
 print("b is greater")
 print("b=",b)

elif c>d:
 print("c is greater")
 print("c=",c)
else:
 print("d is greater")
 print("d=",d)