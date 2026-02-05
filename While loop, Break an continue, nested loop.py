'''#while
is_failed = True
i = 1 #attempt

while is_failed:      #condiion three
    if i%2!=0:  # is not even
        i = i + 1
        continue 
    print(f"Attempt {i}")
    i = i + 1
    if i>100:
        break
print ("I gave up")

#while loop
i = 0

while i<=10:         #attempts == iteration  1
    print("Adrsha"*i)
    i += 1

i = 0

while i<=10:                  ##attempts == iteration  2
    x = 0
    while x<i:
        print("Adrsha", end="-")
        x += 1
    print("")   #enter 
    i += 1
'''
pin = "1234"
trails = 0

while trails<3:
    input_pin = input(f"Trail-{trails} | Pin >> ")
    trails += 1
    if input_pin == pin:
        print("CORRECT")
        break
    else:
        print("INCORRECT")