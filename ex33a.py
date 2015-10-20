# a function that when called will demonstrate the while loop and produce a list

def numbers(x):
	i = 0
	numbers = []
	while i < x:
		print "At the top i is %d" % i
		numbers.append(i)

		i += 1
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i

	print "The numbers: "

	for num in numbers:
		print "The list of numbers: ", numbers

numbers()