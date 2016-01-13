# this python program instructs the user on complex strings
# declares variable and assigns it to a string

x = "There are %d types of people." % 10 # oh dear, I think we know where this is heading

#variables with string assignments
binary = "binary"
do_not = "don't"

#variable assisgned to a string that calls other variables assigned strings
y = "Those who know %s and those who %s." % (binary, do_not)

# variables called from print
print x
print y

# called again within new strings
print "I said: % r." % x
print "I also said: '%s'." % y

# variable assigned a boolean value
hilarious = False

#variable called within the assignment of another variable with formatter
joke_evaluation = "Isn't that joke so funny?! %r"

#both variables called using formatter
print joke_evaluation % hilarious

#variables assigned strings
w = "This sis the left side of..."
e = "a string with a right side."
#variables concantenated
print w + e 
