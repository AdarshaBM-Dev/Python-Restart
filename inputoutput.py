age = input("Enter your age: ")
print("You entered:", age)

#concatination
first_name = "Adarsha"
last_name = "Kumar"
full_name = first_name + " " + last_name
print("Full name:", full_name)

message = "Warning!"
print(message * 3) #repeating the string 3 times

print(message.upper()) #converting to uppercase
print(message.lower()) #converting to lowercase 
print(message.replace("Warning", "Alert")) #replacing a substring
print(message.split("!")) #splitting the string into a list
print(message.strip("!")) #removing leading and trailing characters
print(message.startswith("Warn")) #checking if the string starts with a substring
print(message.endswith("!")) #checking if the string ends with a substring
print(message.find("Warn")) #finding the index of a substring
print(message.count("!")) #counting the occurrences of a substring
print(message.isalpha()) #checking if the string contains only alphabetic characters

#INDEXING
print(message[0]) #accessing the first character
print(message[-1]) #accessing the last character
print(message[2:5]) #accessing a substring (slice)
print(message[::2]) #accessing every second character
print(message[::-1]) #reversing the string
print(len(message)) #getting the length of the string

#escape characters
print("This is a \"quote\" inside a string.") #using escape character for double quotes
print('This is a \'quote\' inside a string.') #using escape character for single quotes
print("This is a backslash: \\") #using escape character for backslash
print("This is a new line:\nThis is the second line.") #using escape character for new line
print("This is a tab:\tThis is after the tab.") #using escape character for tab
print("This is a carriage return:\rThis will overwrite the line.") #using escape character for carriage return