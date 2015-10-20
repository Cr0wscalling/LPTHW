print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
	print "There's a giant bear here eating a cheese cake. What do you do?"
	print "1. Take the cake."
	print "2. Scream at the bear."
	print "3. Use the bear spray on the counter!"


	bear = raw_input("> ")

	if bear == "1":
		print "The bear eats your face off. Good job!"

	elif bear == "2":
		print "The bear eats your legs off. Good job!"

	else:
		print "Well , doing %s is probalby better. Bear runs away." % bear

if door == "2":
	print "You see a soft bed next to a gently burning fire. What do you do?"
	print "1. Lay down and have a nice nap"
	print "2. Sit down by the fire and reflect on the day"
	print "3. Is that a bear in the next room? I think I'd better keep moving"

	choice = raw_input("!!!>")
