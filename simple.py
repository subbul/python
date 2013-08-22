#import modules used here
import sys

def main():
	print 'Hello there',sys.argv[1]



#standard boilter plate
# __name__ will be main only when directly execute, but not when include or imported by another module
if __name__ == '__main__':
	main()
