import math
A,B,C = input().split()
A,B,C = [int(i) for i in [A,B,C]]

x = (-B) + (math.sqrt((B**2)-(4*A*C)))/ 2*A
x1 = (-B) - (math.sqrt((B**2)-(4*A*C)))/ 2*A

print(round(x,2))
print(round(x1,2))
