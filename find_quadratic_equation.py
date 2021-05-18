"""python program for Quadratic equation"""

import cmath

a= int(input("enter a"))
b=int(input("enter b"))
c=int(input("enter c"))
# calculate the discriminant
d = (b**2) - (4*a*c)

# find two solutions
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('The solution are {0} and {1}'.format(sol1,sol2))