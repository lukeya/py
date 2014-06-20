tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

#while True:
#    for i in ["/","-","|","\\","|"]:
#        print "%s\r" % i,

complex = "This is a %s string."
print complex % "\n\\complex\\"

escape_r = "One escape %r."
print escape_r % "\tsequence"
escape_s = "One escape %s."
print escape_s % "\tsequence"

print "/"