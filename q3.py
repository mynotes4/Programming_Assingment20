"""
Question3
Create a function that takes the height and radius of a cone as arguments and returns the
volume of the cone rounded to the nearest hundredth. See the resources tab for the formula.
Examples
cone_volume(3, 2) ➞ 12.57
cone_volume(15, 6) ➞ 565.49
cone_volume(18, 0) ➞ 0
"""

from math import pi

def cone_volume(h,r):
    return round((pi * r * r * h) / 3,2)

h = float(input("Enter height of cone "))
r = float(input("Enter radius of cone "))
v = cone_volume(h,r)
print("cone_volume(",h, r,") ➞",v)