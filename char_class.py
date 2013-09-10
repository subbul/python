### char class

import re
match = re.findall("[\s,.]","Hello this is, good.") #if you use find only it will stop at first match

if match:
	print "Matched string",match
else:
	print "Failed to match pattern"


match = re.search("[\s,.]+","Hello this is, good.") #if you use find only it will stop at first match

if match:
	print "Matched string",match.group()
else:
	print "Failed to match pattern"