num = int(input("Enter the number: "))
fact = 1

for i in range(1, num):
    fact *= i;

print("Factorial of {} is {}".format(num, fact))