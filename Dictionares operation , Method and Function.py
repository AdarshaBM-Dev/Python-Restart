#dictionary

birthday = {
    "Adarsha": "03-03-2003",     #keys : values
    "virat": "05-10-1988",
    "Amith": "07-12-2026"
}
print(birthday)
print(type(birthday))

meanings = {
    "bat" : "used  to it",
    "bat" : "this is hit",
    "wicket" : "to be protected"
}

print(birthday["Adarsha"])
print(birthday.get("darshan", "Not found"))

birthday["Krishna"] = "02-09-1973"    #add dictonary
print(birthday)

birthday["Sudeep"] = "02-09-1973"    #add dictonary
print(birthday)

birthday["Amith"] = "03-12-2004"    #update dictonary
print(birthday)

birthday.pop("Sudeep")    #remove dictonary
print(birthday)

x = birthday.pop("Krishna")
print(x)            #variable assain

#del birthday[" sudeep"]  #remve dictionry

print(birthday.keys())
print(birthday.values())
print(birthday.items())

birthday.update(meanings)
print(birthday)
