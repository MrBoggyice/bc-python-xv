'''
    the present count_dict_val function below the dictionary calculates and returns the
    highest number of values int the dictionary while the later nums_dict_val function returns
    the total number of values in the dictionary
    
    ~fortune
    ~Happy Code Review
'''

# I define my dictionary here
mydict = {
        "a": ["john", "bello"],
        "b": ["cow", "goat", "john"],
        "c": [],
        "d": ["two"]
        
    }
    
#This function returns the dictionary with the highest number of values
def count_dict_val():
    count = 0
    for value in mydict:
        	count = len(mydict[value])
    return count


#This function returns the total number of values in the dictionary
def nums_dict_val():
	count = 0
	for value in mydict:
		count += len(mydict[value])
	return count
print nums_dict_val()
print count_dict_val()