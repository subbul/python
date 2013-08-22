import sys
#first line of a function with 3 " and ends with 3 " constitute DocString for  help(module.function)
#to import this function in this module, import runtime_check, dir(runtime_check),help(runtime_check.repeat)
def repeat(s,exclaim):
	"""Repeats the string optionally with exclamation appended
	"""
	result = s + s + s 

	if exclaim:	
		result = result + '!!!'
	return result


def main():
	name = sys.argv[1]
	if name == 'Guido':
		print repeet(name) + '!!!!' # no compile time check for undefined Function name, only runtime
	else:
		print repeat(name,False)

if __name__ == '__main__':
	main()