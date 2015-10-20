def cheese_and_crackers(cheese_count, boxes_of_crackers): # this section preps for the rest of the code body
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"


print "We can just give the function numbers directly:" #this assigns a value to the variable 
cheese_and_crackers(20, 30)


print "OR, we can use variables from our scripts:" # uses variable from the 
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers) #assigns a new value to the funciton def


print "We can even do math inside too:" # uses mathmatical operater to assign new value to fxn def
cheese_and_crackers(10 + 20, 5 + 6)


print "And we can combine the two, variables and math:" # everythin condensed
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)