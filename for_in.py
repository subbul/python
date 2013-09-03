# example for for iteration using for.. in syntax

def sumofSquares(squares):
	""" function to get sum of squares using for..in iteration on lists
	"""
	sum = 0
	for num in squares:
		sum += num
	print "Sum of squares is ", sum

def checkIfPresent(haystack,needle):
	""" check for presence of a string in a list using "if ..in" method
	"""
	if needle in haystack:
		print "Hurray %s is present" %[needle]
	else:
		print "Sorry no luck for %s" %[needle]

def main():
	list = [1,4,9,16]
	sumofSquares(list)

	nameList = ['Tom','Dick','Harry','Jerry']
	checkIfPresent(nameList,'Tom')
	checkIfPresent(nameList,'Ravi')

if __name__ == '__main__':
	main()