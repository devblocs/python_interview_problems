num = int(input("Enter the number: "))
temp = num
result = 0

while temp > 0:
    remainder = temp%10
    result += (remainder**3)
    temp //= 10
    
if(num == result):
    print("{} is an armstrong number".format(num))
else:
    print("{} is not an armstrong number".format(num))
