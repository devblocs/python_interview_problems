num = int(input("Enter the number: "))
a, b, counter = 0,1,0

print("Factorial of {} is:".format(num))
while counter < num:
    print(a, end = ",")
    c = a+b
    a = b
    b = c
    counter += 1




