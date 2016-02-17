#first we import the modulus that enables us to use the reduce function but i use python 2x its commented out
#from functools import reduce
'''
n = 3

ls = (xrange(1, n))
print ls

facto = reduce(lambda x,y: x * y, ls)

print facto'''

n=2 # then we assign n to the value of here
ls = [x for x in range(1, n+1)] # this is a list comprehension that loops the range of n

facto = reduce(lambda x,y: x * y, ls) # this is the reduce function which returns the factorial of n

print facto

'''
	NB. the first parameter of lambda which is x,y:
	where is x is the accumulator and y is the returned
	value

'''