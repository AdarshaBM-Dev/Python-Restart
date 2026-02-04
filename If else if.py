x = 24
if x%2==0:
    print("x is even")
else:
    print("x is odd")


#if ,else ,els

signal = input("what'sthe colour of the sgnal: ")

if signal == "red":  
    print("STOP")
elif signal == "yellow":
    print("READY")
elif signal == "green":
    print("GO")
else:
    print("INVALID")


#nested 
gender = input("gender: ")
age =int(input("Enter yourr age: "))

if gender == "female":
    print("ticket is free")
else:
    if age < 5:
        print("Ticket is free")
    elif age <= 12:
        print("You get a child discount. Half price")
    elif age >= 60:
        print("You get a senior citizen discount.")
    else:
        print("You pay the ful fare.")
