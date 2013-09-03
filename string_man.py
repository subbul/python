def simple_strings():
	s = "hello"
	print s+''+"world"
	print "original",s

	#s+1 # should throw error
	print s+str(1) # should be fine

	raw = r'here\n there \t'
	print raw

	multi = """ Multiline
	               next line """
	print multi


def string_ops():
	s = "Hello World"
	print "Lower case", s.lower()
	print "Upper case", s.upper()
	s = 'A'
	print "Is Alpha only",s, s.isalpha()
	s = '1'
	print "Is Digit only",s, s.isdigit()
	s = '  '
	print "Is space",s, s.isspace()
	s= 'ABCDEFGHIJKL'
	print "Does it starts with A",s,s.startswith('A')
	print "Does it ends with Z",s,s.endswith('Z')
	print "Find F",s, s.find('F');
	s = "he is a good, he is strong"
	print s,"<==replaced string==>",s.replace('he','she')

def main():
	print "Simple Strings"
	simple_strings()
	print "String manipulation"
	string_ops()
	
if __name__ == '__main__':
	main()