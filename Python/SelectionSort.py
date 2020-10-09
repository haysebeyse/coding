# Import required modules

import timeit
from random import seed
from random import randint

# Define function which finds lowest value in an array
def findLowestValue(arr):
	lowest=arr[0]
	lowestIndex=0
	for i in range(len(arr)):
		if arr[i]<lowest:
			lowest=arr[i]
			lowestIndex=i
	return lowestIndex

# Define selection sort function	
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