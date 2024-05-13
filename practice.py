# Consider the following expression

a = not True and False or True
print(a)

# WAP to print the greatest of the three numbers
x = int(input("Enter the 1st number: "))
y = int(input("Enter the 2nd number: "))
z = int(input("Enter the 3rd number: "))
if (x>y) and (x>z):
    print("The biggest number is:", x)
elif (y>x) and (y>z):
    print("The biggest number is:", y)
else:
     print("The biggest number is:", z)
    

   
    