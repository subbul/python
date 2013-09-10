import re
match = re.search("\d","Abcd1234")
if match:
	print "String", "Abcd1234"
	print "Searching for \d - search and return first decimal", match.group()
else:
	print "No,Match for \d - decimal search failed"


match = re.search("\D","Abcd1234")
if match:
	print "String", "Abcd1234"
	print "Searching for \D - search and return first non-decimal ", match.group()
else:
	print "No,Match for \D- non-decimal search failed"

match = re.search("\s","Abcd 1234")
if match:
	print "String", "Abcd 1234"
	print "Searching for \s - search and return first whitespace char(space, tab, newline) ", match.group()
else:
	print "No,Match for \s- first whitespace char(space, tab, newline search failed"


match = re.search("\S","Abcd 1234")
if match:
	print "String", "Abcd 1234"
	print "Searching for \S - search and return first NON whitespace char(space, tab, newline) ", match.group()
else:
	print "No,Match for \S- first NON whitespace char(space, tab, newline search failed"

match = re.search("\w","Abcd 1234")
if match:
	print "String", "Abcd 1234"
	print "Searching for \w- search and return first alphanumeric(a-z,0-9) ", match.group()
else:
	print "No,Match for \w first first alphanumeric(a-z,0-9) failed"

match = re.search("\W","Abcd# 1234")
if match:
	print "String", "Abcd# 1234"
	print "Searching for \W- search and return first NON alphanumeric(a-z,0-9) ", match.group()
else:
	print "No,Match for \W- first NON alphanumeric(a-z,0-9) failed"
