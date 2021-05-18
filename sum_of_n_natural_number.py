"""python program for sum of n natural number """

# get input from the user

n=int(input("enter the n number"))
sum=0
##sum of n natural number
for i in range(1,n+1):
    sum=sum+i

print("sum of ",n, "nautral number is",sum)
  