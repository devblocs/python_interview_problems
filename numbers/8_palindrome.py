num = int(input("Enter the number: "))
temp = num
result = 0

while temp > 0:
    rem = temp%10
    result = rem + (result*10)
    temp //= 10
    
if(num == result):
    print("{} is a palindrome number".format(num))
else:
    print("{} is not a palindrome number".format(num))
    