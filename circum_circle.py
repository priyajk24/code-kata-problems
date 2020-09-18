import math
A = float(input())

if A<0:
    print("Error")
else:
    A = 2*math.pi*A
    print(round(A,2))
