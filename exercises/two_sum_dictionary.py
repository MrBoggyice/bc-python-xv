'''
    so i actually started my code review with Jolade and Emeka
    on the two_sum dictionary loop and below is Jolade's code
    while the later is Emeka's code which includes, and what 
    this piece of code does is that within a range nums which is the
    first paremeter it returns the index of the numbers which are the
    sum of the target which is the second parameter

    ~fortune
    ~Happy code review 
'''

#jolade's code 
def two_sum(nums,target):
    count = 0
    mydict={}
    for i in range(len(nums)):
        key = target - nums[i]
        #print(nums[i])
        print(key)
        #ind = i
        if(key in mydict):
           
            return [mydict[key],i]
        else:

            #print (i)
            mydict[nums[i]] = i
            print(mydict)
    #count+=1

#print(two_sum([2,5,1,7,3,58,12],14))
print(two_sum([2,5,1,7,78,54,56,32,55,10,200,100],300))

#Emeka's code           
def twosum(nums,target):
   dict_hold = {}
   for idx in nums:
       tar = target - idx
       if tar in dict_hold:
           #print ([dict_hold[tar],nums.index(idx)])
           return [dict_hold[tar],nums.index(idx)]
       else:
           dict_hold[idx] = nums.index(idx)
twosum([1,2,3,5],8)

