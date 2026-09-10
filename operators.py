#operators

#assignment operator
x = 5  # Assigns 5 to x
x += 3  # Equivalent to x = x + 3, now x is 8
x -= 2  # Equivalent to x = x - 2, now x is 6
x *= 4  # Equivalent to x = x * 4, now x is 24
x /= 6  # Equivalent to x = x / 6, now x is 4.0
print("Final value of x:", x)  # Outputs: Final value of x: 4.0

#comparison operators
y = 10  # Assigns 10 to y
print("x == y:", x == y)  # Outputs: x == y: False
print("x != y:", x != y)  # Outputs: x != y: True
print("x < y:", x < y)    # Outputs: x < y: True
print("x > y:", x > y)    # Outputs: x > y: False
print("x <= y:", x <= y)  # Outputs: x <= y: True
print("x >= y:", x >= y)  # Outputs: x >= y: False

#aruthmetic operators
a = 15  
b = 4
print("a + b:", a + b)  # Outputs: a + b: 19
print("a - b:", a - b)  # Outputs: a - b:   11
print("a * b:", a * b)  # Outputs: a * b: 60
print("a / b:", a / b)  # Outputs: a / b: 3.75
print("a // b:", a // b)  # Outputs: a // b: 3
print("a % b:", a % b)  # Outputs: a % b: 3             

#logical operators
p = True
q = False
print("p and q:", p and q)  # Outputs: p and q: False
print("p or q:", p or q)    # Outputs: p or q: True
print("not p:", not p)      # Outputs: not p: FalseS

#membership operators
list1 = [1, 2, 3, 4, 5]
print("3 in list1:", 3 in list1)  # Outputs: 3 in list1: True
print("6 not in list1:", 6 not in list1)  # Outputs: 6 not in list1: True

#bitwise operators
c = 10  # Binary: 1010
d = 6   # Binary: 0110
print("c & d:", c & d)  # Outputs: c & d: 2   (Binary: 0010)
print("c | d:", c | d)  # Outputs: c | d: 14  (Binary: 1110)
print("c ^ d:", c ^ d)  # Outputs: c ^ d: 12  (Binary: 1100)
print("~c:", ~c)        # Outputs: ~c: -11 (Binary: ...11110101)