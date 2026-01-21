'''
print('Love') #output
#age = input("Age: ")   #input
#print(age)

boy_name = input("Boy Name >> ")
boy_age = int(input("Boy Age >> "))
girl_name = input("Girl Name >> ")
girl_age = int(input("Girl Age >> "))
age_diff = abs(boy_age - girl_age)              #abs - absolute value - or +

print(f"{boy_name} loves {girl_name}. Age Difference is {age_diff}")

'''

#concantination
first_name = "Adarsha"
middle_name = "Krishna"
last_name = "Wadiyar"
full_name = first_name + " " + middle_name + " " + last_name
print(full_name)

#repataion 
message =" This is Warning!"
print(message * 100)

print(message.upper()) 
print(message.lower())
print(message.strip())
print(message.replace("Warning", "Error"))

#inducting
name = "Adarsha"
print(name[4])   #index = position - 1
print(name[2:4])
print(name[:6])
print(name[2:])
print(name[-4])
print(name[1:6:2])    #[start:end:step or skip]
print(name[::2])

s = "Adarsha \n is \t a good boy"
print(s)

