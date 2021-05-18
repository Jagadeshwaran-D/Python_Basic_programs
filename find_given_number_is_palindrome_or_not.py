"""python program for find given number is palindrome or not """
#get input from the user
number=int(input("enter the number"))
copy_of_number=number
sum=0
#reverse the given number
while(number!=0):
    rem=number%10
    sum=(sum*10)+rem
    number=number//10
#check palindrome or not
if copy_of_number==sum:
    print(copy_of_number,"is palindrome")
else:
    print(copy_of_number,"is not palindrome")
