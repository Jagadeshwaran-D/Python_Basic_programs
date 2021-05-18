"""  python program  for print all prime numbers in given interval   """

#take input from the user
a=eval(input("enter the number"))
#check numberr is greater than 1
if a>1:
    print(1)

    #code for find prime number
for i in range(0,a+1):
   b=0
   for j in range(1,a+1):
      if i%j==0:
          b=b+1

   if b==2:
      print(i )
   
