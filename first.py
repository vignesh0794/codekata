num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
num3 = input("Enter third number: ")
 
if (num1 > num2) & (num1 > num3):
   largest = num1
elif (num2 > num1) & (num2 > num3):
   largest = num2
else:
   largest = num3
 
print("The largest number is",largest)
