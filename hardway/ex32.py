the_count = [1,2,3,4,5]
fruits = ["apples", "oranges","pears","apricots"]
charge = [1,"pennies",2,"dimes",3,"quarters"]

for number in the_count:
	print "This is count %d." % number

for fruit in fruits:
	print "This is fruit of type: %s" % fruit

for i in charge:
	print "I got %r." % i

elements = []

for i in range(0,6):
	print "Adding %d to the list." % i
	elements.append(i)

for i in elements:
	print "Element was %d." % i