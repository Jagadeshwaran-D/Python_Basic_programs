""""python program for find greatest of three numbers"""
#take input from the user
first_number=eval(input("enter first number"))
second_number=eval(input("enter second numberr"))
third_number=eval(input("enter third number"))


#find largest of three number
if first_number>second_number and first_number>third_number:
    print(first_number,"is greatest number")
elif second_number>third_number:
    print(second_number,"is greatest number")
else:
    print(third_number,"is the greatest number")