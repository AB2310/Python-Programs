x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
o = input("Enter +, -, *, /: ")

if o == "+" :
    result = x+y
elif o == "-" :
    result = x-y
elif o == "*" :
    result = x*y
elif o == "/" :
    if y==0 :
        print("Division by 0 is not possible")
    result = x/y

print(result)
    