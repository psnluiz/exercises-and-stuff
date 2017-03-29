while True:
    try:
        tempFar = int(input("Enter the temperature in Farenheit: "))
    except ValueError:
        print("Woops, it seems an error has occurred.Please type ONLY the numbers in the temperature")
    print ("The temperature in Celsius is: ", (tempFar - 32)/9 * 5)

        
        
