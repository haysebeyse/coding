'''
Selection Sort Algorithm O(n^2):
	1. Scan entire list and find the lowest (or highest) number.
	2. Move this number to the beginning (or end) of a new list to form sorted array.


'''

import timeit
from random import seed
from random import randint

# Find index of lowest value
def findLowestValue(arr):
	lowest=arr[0]
	lowestIndex=0
	for i in range(len(arr)):
		if arr[i]<lowest:
			lowest=arr[i]
			lowestIndex=i
	return lowestIndex

# Form the sorted array based on lowest values
def sortAscending(arr):
	sortedArr=[]
	for _ in range(len(arr)):
		ind=findLowestValue(arr)
		sortedArr.append(arr.pop(ind))
	return sortedArr

# Generate a random integer array
arr=[]
seed(1)
for _ in range(15):
	arr.append(randint(10, 99))
print("Unsorted Array: ", "\t", arr)

# Sort array and calculate exec time
st=timeit.default_timer()
sorted=sortAscending(arr)
sp=timeit.default_timer()

# Print results
print("Sorted Array: ", "\t", sorted)
print("Time: ", "\t\t\t\t", "{:.4f}".format((sp-st)*1e3), "ms")