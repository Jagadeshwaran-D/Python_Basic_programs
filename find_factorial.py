""" python program  for factorial of given number"""

num=eval(input("enter the number"))
factorial=1
for i in range(1,num+1):
  factorial*=i

print("Factorial of " ,num,"is",factorial )