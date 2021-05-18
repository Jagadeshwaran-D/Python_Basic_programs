"""  python program  for given number is  prime number or not   """

#take input from the user
a=eval(input("enter the number"))
b=0
for j in range(1,a+1):
      if a%j==0:
          b=b+1
if b==2:
      print(a,"is prime number" )
else:
    print(a,"is non prime number")
   
