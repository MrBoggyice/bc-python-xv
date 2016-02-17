'''
	wow! it's cool to call a function by it's 
	but very dangerous when you miss the base
	case because it could crash your browser
	so this recursion, which means calling a
	function in terms of itself...

	~fortune
	~~Happy Code review geeks

'''

def recur_fact(n):
	if n == 0 or n == 1:
		return 1
	else:
		return n * recur_fact(n-1)


print recur_fact(8)