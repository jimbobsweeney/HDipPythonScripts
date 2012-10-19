from sys import argv

script, filename = argv

txt = open(filename)

print "Here's file %r. Enjoy it." % filename
print txt.read()
txt.close()

print "Type that filename again:"
file_again = raw_input('> ')

txt_again = open(file_again)
print txt_again.read()
txt_again.close()