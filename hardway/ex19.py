def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers" % boxes_of_crackers
	print "Man, that's enough for a party!"
	print "Get a blanket.\n"

print "We can just give the function numbers directly."
cheese_and_crackers(30,40)

print "OR we can use variables from our script"
amount_of_cheeses = 18
amount_of_crackers = 35
cheese_and_crackers(amount_of_cheeses,amount_of_crackers)

print "We can even do maths inside too."
cheese_and_crackers(20+15,35-18)

print "And we can combine the two, variables and maths."
cheese_and_crackers(amount_of_cheeses + 100, amount_of_crackers+1000)