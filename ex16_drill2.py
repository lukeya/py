from sys import argv
script, filename = argv

file = open(filename, 'r')
txt = file.read()
print txt
file.close()