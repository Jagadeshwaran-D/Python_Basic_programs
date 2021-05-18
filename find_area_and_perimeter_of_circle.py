"""python program for find area & circumference of circle  """


##function for calculate area of circle
def get_areaof_circle(radius):
     area=radius*radius*3.14
     return area


##function for calculate circumference of circle
def get_circumference_circle(radius):
 circumference=2*3.14*radius
 return circumference

radius=eval(input("Enter the radius "))
##calling the function for find area& perimeter of circle
print("area of circle " + str(get_areaof_circle(radius)))
print("circumference of  circle " + str(get_circumference_circle(radius)))
 

