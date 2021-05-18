"""python program for find area & perimeter of triangle  """


##function for calculate area of triangle
def get_areaof_triangle(base,height):
     area=(base*height)/2
     return area




###get input from the user

base=int(input("enter the base"))
height=int(input("enter the height"))

##calling the function

print(" Area of triangle is " ,get_areaof_triangle(base,height))

