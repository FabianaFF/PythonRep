# -- coding: utf-8 --

my_name = "Fabiana Fraga"
my_age = 29
my_height = 74 #inches
my_weight = 180
my_eyes = "Green"
my_teeth = "White"
my_hair = "Red"

print "Let's talk about %s." % my_name
print "She's %d inches tall." % my_height
print "She's %d pounds heavy." % my_weight
print "Actually that´s not too heavy."
print "She's got %s eyes  and %s hair." % (my_eyes,my_hair)
print "Hers teeth are usually %s depending on the cofee." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." %(
		my_age, my_height, my_weight, my_age + my_height + my_weight)
