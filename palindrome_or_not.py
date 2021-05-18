"""python program for given string is palindrome or not """


##function for check palindrome or not
def check_palindrome(string):
    reverse=string[::-1]
    if string==reverse:
        print("It is palindrome")
    else:
        print(" It is not a palindrome")
    return reverse
##get input from the user 
string= input("enter ")
##calling the function for checking palindrome or not
check_palindrome(string)