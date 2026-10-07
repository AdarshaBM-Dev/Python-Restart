#if
x = 10
if x == 10:
    print("yes s is 10")

#else
x = 24
if x%2 == 0:
    print("x is even")
else:
    print("x is even")

#if-else-elif
signal =input("What is the colour  of the signal:  ")

if signal == "red":
    print("STOP")
elif signal == "yello":
    print("READY")
else:
    print("GO")



att = input("what is your att percentage:   ")

if att >= 75:
    print("exam")
elif att <75 and is_teacher_frend == True:
    print("exam")
else:
    print("no exam")



age = input("age:   ")

if age < 5:
    print("Ticket is free.")
elif age <= 12:
    print("You get a child discount.")
elif age >= 60:
    print("You get a senior citizen discount.")
else:
    print("You pay the full fare.")