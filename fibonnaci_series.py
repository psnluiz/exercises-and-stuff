while True:
    a, b = 1, 1
    k = 1
    num = int(input("N: "))
    while (k <= num-2):
        a, b = b, a+b
        k += 1
    print(b)
