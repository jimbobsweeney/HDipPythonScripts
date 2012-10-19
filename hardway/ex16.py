from sys import argv

script, filename = argv

print "We are going to erase %r" % filename
print "If you don't want to, hit Ctrl-C."
print "If you do, hit Return."

raw_input("?")

print "Opening the file"
target = open(filename, 'w')

print "Truncating the file. Gooooooodbyeee!"
target.truncate()

print "Now, type in three new lines."
line1 = raw_input("Line 1: ")
line2 = raw_input("Line 2: ")
line3 = raw_input("Line 3: ")

print "Thank you. Now I'ma write them to %r." % filename

target.write(line1+"\n"+line2+"\n"+line3)

print "Job done. And now I'ma close the mother."
target.close()

print "Thanks for that. I feel much better now."