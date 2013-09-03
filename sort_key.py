#sorting a list with custom keys

strs = ['ccc','ddd','aaa','b','dd']
print "Original string list", strs;
print "Strings sorted using length as key function",sorted(strs,key=len)