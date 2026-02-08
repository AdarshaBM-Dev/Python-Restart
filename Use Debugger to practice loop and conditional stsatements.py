#debugging



#i = 0
#while i<=5:
 #   print(i, end = " ")
  #  i += 1


#for i in range(1, 3):
#   for j in range(1,11):
#       print(f"{i}X{j}={i*j}")

l = [1, 23, 323, 1231, 123]
cl =[]

for i in range(len(l)):
    c = l[i]
    d = l[-i]
    x = c*d
    if x%2==0:
        cl.append(x)
print(cl)