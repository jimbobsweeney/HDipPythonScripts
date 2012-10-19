#!/usr/bin/python

class Rect(object):
	"""This is a class representing a rectangle."""
	def __init__(self, width, height):
		self.width = width
		self.height = height

	def getArea(self):
		return self.width*self.height

	def getPerimeter(self):
		return (self.width*2) + (self.height*2)

def main():
	this_rectangle = Rect(20,30)
	print "A rectangle has been created of height %d and width %d." %\
	(this_rectangle.height, this_rectangle.width)

	this_area = this_rectangle.getArea()
	print "The area of this rectangle is %d." % this_area

	this_perimeter = this_rectangle.getPerimeter()
	print "The perimeter of this rectangle is %d." % this_perimeter

if __name__ == '__main__':
	main()