# version 5a includes conversion from  US imperial to metric and uses the method round
name = 'Zed A. Shaw'
age = 35 # not a lie
heightUS = 74 # inches
weightUS = 180 # lbs
metric_Height = round(heightUS * 2.4)
metric_Weight = round(weightUS / 2.2)
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s" % name
print "He's %d inches tall (thats %d centimeters.)" % (heightUS, metric_Height)
print "He's %d pounds heavy (thats %d kilos)." % (weightUS, metric_Weight)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on th coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d (thats %d with metric units.)" % (age, heightUS, weightUS, age + heightUS + weightUS, age + metric_Height + metric_Weight)



