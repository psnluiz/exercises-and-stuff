#x = tempo em minutos 
try:
    x = int(input("Tempo gasto em minutos: "))
except ValueError:
    print ("Ops, um erro ocorreu...Digite apenas números!")
if (x < 200):
    print ("O valor da conta é: ", (x * 0.2))
else:
    if (x <= 400):
        print ("O valor da conta é: ", (x * 0.18))
    else:
        if (800 >= x > 400):
            print ("O valor da conta é: ", (x * 0.15))
        else:
            print ("O valor da conta é: ", (x * 0.08))
            
            


