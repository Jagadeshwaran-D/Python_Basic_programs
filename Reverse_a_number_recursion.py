""" python program for reverse a given number using recursion"""
 # initial value is 0. It will hold the reversed number
sum=0

#logic for reverse a number  
def reverse_number(a):
    global sum
    if(a!=0):
        rem=a%10
        sum=(sum*10)+rem
        reverse_number(a//10)
    return sum
a=eval(input("enter the number"))

print(reverse_number(a))
