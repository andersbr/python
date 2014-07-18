# Lesson 5: Fizz Buzz Refactor
# Bryan Anderson

import sys

#sys.argv[0] is filename of script, counts as first argument
# start cmd line args at sys.argv[1}

print "The name of this script is {}".format(sys.argv[0])
print "User supplied {} args at run time".format(len(sys.argv))

for arg in sys.argv[1:]:
	print arg

while True:
	try:
		if len(sys.argv) == 1:
			ulimit = raw_input("Type a positive integer")
			ulimit = int(ulimit)
			break
		else:
			ulimit = int(sys.argv[1])
			break
	except ValueError:
			print "Integers Only! Try Again!"
			ulimit = raw_input("Type a positive integer")
			ulimit = int(ulimit)
			break
	
def is_dev(x,y):
	return x % y == 0

def fizz_buzz(i=100):
	for i in range(0,ulimit):
		i = i+1
		if is_dev(i,15):
			print "fizzbuzz"
		elif is_dev(i,3):
			print "fizz"
		elif is_dev(i,5):
			print "buzz"
		else:
			print i


if __name__ == '__main__':
	fizz_buzz(ulimit)