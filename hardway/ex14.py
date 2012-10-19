from sys import argv
script, user_name = argv

prompt = '> '
print "Hi %s, I'm the %s script." % (user_name,script)
print "I'd like to aks you a few questions."
print "Do you like me, %s?" % user_name
likes = raw_input(prompt)

print "Where do you live, %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me. Fair enough.
You live in %r. Not sure where that is, but never mind.
You have a %r computer. Nice!
""" % (likes, lives, computer)