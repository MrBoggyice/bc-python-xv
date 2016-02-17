def odd_numbers(low, bound):
		for i in range(low, bound):
		if i % 3 == 0:
			return i
		else:
			print "not an odd number prolly"

print odd_numbers(2, 10)