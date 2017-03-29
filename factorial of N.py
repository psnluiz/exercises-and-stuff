num = int(input("Type a number: "))
b = (num-1)
result = 1
while (b > 0):
    result = result * (num * b)
    num -= 2
print("The factorial of {} is {}".format(num, result))
