while True:
    n = int(input("Type a number: "))
    n_2 = n
    c = 1
    result = 1
    while (n_2 - c >= 1):
        result = result * ( n_2 * (n_2 - c))
        n_2 -= 2
    print ("The factorial of {} is {}".format(n, result))

   
 
