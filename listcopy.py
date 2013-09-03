# simple list

colors = ['red','blue','green']

print "Print the entire color palette",colors
b = colors # just a reference or pointer not deep copy

print "Print copy b" , b
colors[0] = 'yellow'

print "Print modified colors",colors
print "Print b ",b     # will point to what colors have

b = colors[:] # deep copy of colors into b

colors[0] = 'red'

print "Again print colors",colors

print "Print b which is a deep copy of colors",b
