""" python program for reverse a given number """

# Initiate value to null  
sum=0
#logic for reverse a number  
a=eval(input("enter the number"))
while(a>0):
    rem=a%10
    sum=(sum*10)+rem
    a=a//10

    #print the output
print(sum)
