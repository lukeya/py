from sys import argv
from os.path import exists

script, from_file, to_file = argv


#Could do these two on one line too.
in_file = open(from_file)
indata = in_file.read()
#print len(indata)
#print "The input file is %d bytes long" % len(indata)

if not exists(to_file):
    print "The output file doesn't exist. Created one."
#print "Ready, hit RETURN to continue, CTRL-C to abort"
#raw_input()

out_file = open(to_file, 'w')
print "Copying from %s to %s" % (from_file, to_file)
out_file.write(indata)

print "Alright, all done."

out_file.close()
in_file.close()