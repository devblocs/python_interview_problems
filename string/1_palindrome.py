text = input("Enter the string: ")
result = ""

# using for loop
for i in text:
    result = i + result
    
print(result)

# using substring
print("The reverse of string '{}' is '{}' \n".format(text, text[::-1]))

if(text == text[::-1]):
    print("'{}' is a palindrome string".format(text))
else:
    print("'{}' is not a palindrome string".format(text))