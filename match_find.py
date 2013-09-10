import re
m = re.match("super","superlative")

print "string  superlative"

if m:
	print "match:string found", m.group()
else:
	print "match:String not found"


print "string insuperable"
m = re.match("super","insuperable")

if m:
	print "match:string found", m.group()
else:
	print "match:String not found"

m = re.search("super","superlative")

print "string  superlative"

if m:
	print "Using search :string found", m.group()
else:
	print "String not found"


print "string insuperable"
m = re.search("super","insuperable")

if m:
	print "Using search :string found", m.group()
else:
	print "String not found"

