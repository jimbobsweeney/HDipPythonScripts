print "You enter a dark room with two doors. Do you go through door no. 1 or door no. 2?"

door = raw_input("> ")

if door == "1":
	print "There's a giant bear here eating a cheese cake. What do you do?"
	print "1. Take the cake."
	print "2. Scream at the bear."

	bear = raw_input("> ")

	if bear == "1":
		print "The bear eats your face off. Good job!"
	elif bear == "2":
		print "The bear eats your legs off. Good job!"
	else:
		print "well, doing %s is probably better. The bear runs away." % bear

elif door == "2":
	print "You stare into the endless abyss at Cthulhu's retina."
	print "1. Blueberries."
	print "2. Yellow Jacket Clothespins."
	print "3. Understanding revolvers yelling melodies."

	insanity = raw_input("> ")

	if insanity == "1" or insanity == "2":
		print "Your body survives, powered by a mind of jelly. Good job!"
	else:
		print "The insanity rots your eyes into a pool of mush. Good job!"

else:
	print "You stumble around, fall on a knife and die. Good job!"