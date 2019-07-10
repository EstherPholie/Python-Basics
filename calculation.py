import math
import datetime

pi = math.pi
degree = float(input("Enter degrees\n"))
radian = degree * (pi/180)
print(f"Radian = {radian}")

radius = float(input("Input radius\n"))
surface_area_of_sphere = 4 * pi * math.pow(radius, 2)
volume_of_sphere = 4/3 * pi * math.pow(radius, 3)
print(f"Surface Area of a Sphere = {surface_area_of_sphere}")
print(f"Volume of a Sphere =  {volume_of_sphere}")

today = datetime.date.today()
now = datetime.datetime.now()
print(f"Today's date = {today}")
print(f"Time = {now}")

