def even_numbers(low, bound):
	for i in range(low, bound):
		if i % 3 == 0:
			return i
		else:
			print "probably not an odd number"

print even_numbers(2, 10)