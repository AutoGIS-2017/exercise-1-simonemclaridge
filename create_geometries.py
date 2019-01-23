#!/usr/bin/env python3
'''Exercise-1: Working with Geometric Objects

Usage:
    ./create_geometries.py

Author:
    Simone Claridge - 01.22.2019
'''




# Import necessary geometric objects from shapely module
from shapely.geometry import Point, LineString, Polygon


def createPointGeom(x_coord, y_coord):
	# creates a shapely point from parameters
	point = Point(x_coord, y_coord)
	return point


def createLineGeom(points):
	# checks to see if list contains shapely points
	for point in points:
		if type(point) == Point:
			isPoints = True
			continue
		else:
			# if non point found in list, print error message
			print("Error: " + str(point) + ' is not a point')
			isPoints = False
			break

	# if list contains only shapely points, create LineString of points
	if (isPoints):
		line = LineString(points)
		return line
	else:
		return "Error: LineString not created"


def createPolyGeom(points):
	isPoints = 0
	isTuple = 0

	# checks to see if list contains shapely points or tuple of points
	for point in points:
		if type(point) == Point:
			isPoints += 1
			continue
		elif type(point) == tuple:
			isTuple += 1
			continue
		else:
			# if non point found in list, print error message
			print("Error: " + str(point) + ' is not a point or a tuple')
			isPoints = False
			break

	# if list contains only shapely points, create polygon of points
	if isPoints == len(points):
		polygon = Polygon([[p.x, p.y] for p in points])
		return polygon
	# if list contains only only tuple coordinates, create polygon of points
	elif isTuple == len(points):
		polygon = Polygon(points)
		return polygon
	else:
		return "Error: Polygon not created"


# creates a shapely point, print x and y coordinates
point1 = createPointGeom(4.6, 2.3)
print(point1)

# list of shapely points
listOfPoints = [Point(2.2, 4.2), Point(7.2, -25.1), Point(9.26, -2.456)]
# list of non points
listOfNotPoints = [12, 'Dog', False]

# creates line from list of points
lineString = createLineGeom(listOfPoints)

# test to see if non point list will produce error
lineString1 = createLineGeom(listOfNotPoints)

# prints the lists
print(lineString)
print(lineString1)

# creates a list of coordinate tuples
listofTuples = [(2.2, 4.2), (7.2, -25.1), (9.26, -2.456)]

polygon1 = createPolyGeom(listOfPoints)
polygon2 = createPolyGeom(listofTuples)

print(polygon1)
print(polygon2)
