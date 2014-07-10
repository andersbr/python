import sys

print "The name of this script is {}".format(sys.argv[0])
print "User supplied {} args at run time".format(len(sys.argv))

for arg in sys.argv[1:]:
	print arg

ulimit = 100

for i in range(0,ulimit):
	i = i+1
	if i % 3 == 0 and i % 5 == 0:
		print "fizzbuzz"
	elif i % 3 == 0:
		print "fizz"
	elif i % 5 == 0:
		print "buzz"
	else:
		print i