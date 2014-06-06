#AreaOfRegularPolygon
from math import tan
from math import pi

def area_of_regular_polygon(number_of_sides, lenght_of_side):
	area = 0.25 * number_of_sides * (lenght_of_side ** 2) / tan(pi / number_of_sides)
	return area

print area_of_regular_polygon(7, 3)