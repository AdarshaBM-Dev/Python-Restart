boy_name = input("Boy Name: ")
boy_age = int(input("Boy Age: "))
girl_name = input("Girl Name: ")
girl_age = int(input("Girl Age: "))

age_diff = abs(boy_age - girl_age) 

print(boy_name + " love " + girl_name + ". Age Difference is " +str( age_diff))
print(f"{boy_name} loves {girl_age}. Age differences is {age_diff}")

#concatination
frist_name = "chndan"
last_name = 'gowda'
full_name = frist_name + " " + last_name
print(full_name)

message = "This is Warning!"
print(message*20)
print(message.upper())
print(message.lower())
print(message.strip()*2)
print(message.replace("Warning!", "Error"))
print(len(message)) #length

name = "chandan"
print(name[4]) #index = position - 1
print(name[2:7])
print(name[:7])
print(name[2:])
print(name[-2])   #[start:end:step]
print(name[::2])
print(name[::3])