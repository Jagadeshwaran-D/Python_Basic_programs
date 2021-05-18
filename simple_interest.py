"""python program for calculate simple interest """

##function for find simple interest
def get_simple_interest(principal,year,interest):
     interest=(principal*year*interest)/100
     return interest


###get input from the user

principal=eval(input("enter principal amount"))
year=eval(input("no of years"))
interest=eval(input("enter interest rate"))


##calling the function to find simple interest
print(get_simple_interest(principal,year,interest))
