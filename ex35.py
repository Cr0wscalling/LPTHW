from sys import exit

def gold_room():
	print "This room is full of gold. How much do you take?"

	next = raw_input("> ")
	if "0" in next or "1" in next:
		how_much = int(next)
	else:
		dead("Man, learn to type a number.")

	if how_much < 50:
		print "Nice, you're not greedy, you win!"
		exit(0)
	else: 
		dead("You greedy bastard!")


def bear_room():
	print "There is a bear here."
	print "The bear has a bunch of honey."
	print "The fat bear is in front of another door."
	print "How are you doing to move the bear?"
	bear_moved = False

	while True:
		next = raw_input("> ")

		if next == "take honey":
			dead("The bear looks at you then slaps your face off.")
		elif next == "taunt bear" and not bear_moved:
			print "The bear hs moved from the door. You can go through it now."
			bear_moved = True
		elif next == "taunt bear" and bear_moved:
			dead("The bears gets pissed off and chews your legs off.")
		elif next == "open door" and bear_moved:
				gold_room()
		else: 
			print ("I got no idea what that means")


def cthulu_room():
	print "Here you see the great and evil Cthhulu, that is the anxiety before bed, the glance into the closet, the creeping sense of doom, the terror of all terrors."
	print "You meet his penetrating gaze and feel reality dissolve around you into a nightmare."
	print "You may choose to flee for you life or offer The Great Dread one a nice mustard sauce to complement your tasty flesh with as he imbibes on your mortal frame."

	next = raw_input(">  ")

	if "flee" in next:
		start()
	elif "offer" in next:
		dead("Lord Cthulu has honored you by eating you first, he was appreciate of the mustard sauce")
	else:
		cthulu_room()


def dead(why):
	print why, "Good job!"
	exit(0)

def start():
	print "You are in a dark room."
	print "There is a door to your right and to your left."
	print "Choose a door to enter."

	next = raw_input("> ")

	if next == "left":
		bear_room()
	elif next == "right":
		cthulu_room()
	else:
		dead("You inaction led to your death by starvation.")


start()











