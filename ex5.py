# -- coding: utf-8 --
name = 'hoohoo'
age = 35
height = 74
weight = 180
eyes = 'Blue'
teeth = "White"
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %r eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

print "If I add %r, %r, and %d I get %d." % (
    age, height, weight, age + height + weight)

lang = "python"
year = 0.5
print "I have been learning %r for %r years." % (lang, year)

pounds = 25
inches = 24
print "%d pounds is equal to %f kilograms." % (pounds, pounds * 0.4536)
print "%d inches is equal to %f centimeters."  % (inches, inches * 2.54)