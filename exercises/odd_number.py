def odd_numbers(low, bound):
		for i in rang(low:bound):
		if i % 3 == 0:
			return i
		else:
			print "there's an error there"

even_numbers(2, 10)