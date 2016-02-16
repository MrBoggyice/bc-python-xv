def even_numbers(low, bound):
	for i in range(low, bound):
		if i % 2 == 0:
			return i
		else:
			print "probably not an even number"

print even_numbers(2, 10)