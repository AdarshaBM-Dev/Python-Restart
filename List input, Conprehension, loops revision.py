
'''
l = [1,23,43,534,32]       #1
total = 0

for num in l:
    print(total)
    total = total + num

print(total)
'''
'''
l = [1,23,43,534,32]  
dl = []

for num in l:
    dl.append(num*2)
    print(dl)
'''
'''
student_marks = {"Anand": 85, "Geeta": 90, "Kumar": 78}

for student, marks in student_marks.items():
    print(f"{student} - {marks}")
'''
'''
students = ["Adarsha", "Rnjitha", "Krshna"]
marks = [100, 90, 78]
    
student_marks = {}

#for index, student in enumerate(students):
    #student_marks[student] = marks[index]
for i in range(len(students)):
    student_marks[students[i]] = marks[i]

print(student_marks)'''

'''
#l = [1,2,3,4,5]  
l = [x for x in range(1,11)]
dl =  [item*2 for item in l]
print(l)
dl =  [item**2 for item in l] #squre
print(dl)
edl = [x**2 for x in l if x%2==0] #even
print(edl)
'''
'''
names = ["Anand","geetha","Kumar"]

d= {name:len(name) for name in names}
print(d)
'''
'''
city_popultion = {
    "Bengaluru": 84,
    "Mysuru": 11,
    "Huballi": 9,
    "Mangluru":5
}
large_cities = {key:value for key,value in city_popultion.items() if value>10}
print(large_cities)
'''

x = input("Enter list of integer: ").split()
l = [int(num) for num in x]
print(l)
