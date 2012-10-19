def addToList(maximum, increment):
	# i = 0
	numbers = []

	start_number = 0
	nobleList = []
	for i in range(0,maximum/increment):
		nobleList.append(start_number)
		start_number += increment

	for i in nobleList:
		print "At the top, i is %d." % i
		numbers.append(i)
		print numbers

	# while i < maximum:
	# 	print "At the top, i is %d." % i
	# 	numbers.append(i)

	# 	i = i+increment
	# 	print "Numbers now:", numbers
	# 	print "At the bottom, i is %d." % i

	print "The numbers:"
	for num in numbers:
		print num

addToList(6, 1)