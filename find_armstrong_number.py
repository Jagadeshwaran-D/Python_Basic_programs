"""python program for given number is armstrong number or not """
import math
#get input from user
number=int(input("enter the number"))
copy_of_number=number
armstrong_nummber=number
sum=0
count=0
#find how many digit 
while(number!=0):
    rem=number%10
    count+=1
    number=number//10

#logic for armstrong number   407=4^3+0^3+7^3

while(armstrong_nummber!=0):
    rem=armstrong_nummber%10
    sum=sum+pow(rem,count)
    armstrong_nummber=armstrong_nummber//10

#check it is armstrong or not

if sum==copy_of_number:
    print(copy_of_number,"is armstrong number")
else:
    print(copy_of_number,"is non amstrong number")


   