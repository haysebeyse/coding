'''
Binary Search Algorithm O(log n):
	1. Ensure number list is sorted.
	2. Guess middle number and eliminate half the remaining numbers.
'''

import numpy as np
from quicksort import quicksort

def guessNumber(list,item):
	low=0
	high=len(list)-1
	
	while low<=high:	#keep guessing until list size is down to 1 element.
		mid=(low+high)//2
		guess=list[mid]	#guess the middle number.
		if guess==item:
			return mid
		if guess>item: 	#guess was too high. new high is mid -1.
			high=mid-1
		else:					 	#guess was too low. new high is low + 1.
			low=mid+1
	return None				#guess does not exist in the list.

list=np.array([23,34,12,88,90,64,3,7,55])
#sortedList=np.sort(list,kind='mergesort')
sortedList=quicksort(list)
index=np.zeros((len(list),), dtype=int)

while True:
        try:
            item = int(input('Enter a number: '))
            break
        except:
            print("Make sure you enter a whole number.")

numberIndex=guessNumber(sortedList,item)

if numberIndex is not None:
	index[numberIndex]=1

print(sortedList)
print(index)