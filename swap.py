#WAP to swap two numbers
#a= 100
#b= 200
a= int(input("Enter a\n"))
b= int(input("Enter b\n"))

print(" before swap a=",a,"and b=",b)

#inline refrencing
a,b=b,a
#traditional
'''c=a
a=b
b=c'''
print(" after swap a=",a,"after swap b=",b)
