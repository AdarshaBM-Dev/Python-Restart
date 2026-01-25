#opearators
#assainment 
a = 10

a += 100 #a = a + 100 short form
a *= 100
a -= 100
print(a)

#comparision oparator

b = 10
c = 100

print(b == c)
print(b >= c)
print(b <= c)
print(b != c) #not equal to

#logical oparator
 
print(True and True)
print(True and False)
print(False and False)
print(True or True)
print(True or False)
print(False or False)
print(not(True))
print(not(False))
print(1>2 or 2>1)

#membership operators
s = "Adarsha"
s2 = "AdarshaBM"
 
print(("c" in s))
print(("M" in s2) and ("c" in s2))
print(("M" in s2) or ("c" in s2))

#bitwise opearator
e = 5
d = 3 

print(e & d)   #AND
print(e | d)   #OR
print(e ^ d)   #XOR
print(~d)      #NOT   
print(e >> d)  #Right shift
print(e << d)  #Left Shift
