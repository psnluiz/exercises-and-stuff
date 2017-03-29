while True:
    try:
        tempCel = int(input("Enter the temperature: "))
        break
    except ValueError:
        print ("Woops...It seems like an error has occurred.Type ONLY the numbers in the temperature")
print ("The temperature in Farenheit is: ", (tempCel / 5) * 9 + 32)

