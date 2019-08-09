num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("Numbers before swapping: ")
print("First number is {}".format(num1))
print("Second number is {}".format(num2))

num1,num2 = num2,num1

print("Numbers after swapping: ")
print("First number is {}".format(num1))
print("Second number is {}".format(num2))