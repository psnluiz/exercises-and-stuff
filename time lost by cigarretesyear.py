cigNum = int(input("How many cigarrettes do you smoke by day?: "))
time = int(input("How long have you been smooking?(years): "))
#Considering that a person lose 10 minutes of life by cigarette unit;
#número de minutos perdidos
time_lost_min = (cigNum * time * 365 * 10)
print ("You have lost a total amount of:", time_lost_min/1440, "days of life.")
