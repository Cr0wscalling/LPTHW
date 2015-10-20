# a function that when called will demonstrate the while loop and produce a list

def numbers(i, j, k, l):
	
	numbers = []
	for number in range(k, l):
		print "At the top i is %d" % i
		numbers.append(i)

		i += j
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i

	print "The numbers: "

	for num in numbers:
		print num

numbers(0, 2, 0, 7)