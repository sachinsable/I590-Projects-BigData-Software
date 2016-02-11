n = raw_input("Enter the value n: ")
for i in range(1, int(n)+1):
	if i % 6 == 0:
		print "fizzbuzz"
	elif i % 2 == 0:
		print "fizz"
	elif i % 3 == 0:
		print "buzz"
	else:
		print i