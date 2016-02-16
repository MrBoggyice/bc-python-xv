def even_numbers(low, bound):
	for low in rang(bound):
		if low % 2 == 0:
			return low
		else:
			print "there's an error there"

even_numbers(2, 10)