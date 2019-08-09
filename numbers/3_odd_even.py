num = int(input("Enter the number: "))
stat = ["even", "odd"]

if num%2 == 0:
    print("{} is an even number".format(num))
else:
    print("{} is an odd number".format(num))


print()
print()
print("{} is an {} number".format(num, stat[num%2]))