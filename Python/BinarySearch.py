import numpy as np

def guessNumber(list,item):
	low=0
	high=len(list)-1
	
	while low<=high:
		mid=(low+high)//2
		guess=list[mid]
		if guess==item:
			return mid
		if guess>item:
			high=mid-1
		else:
			low=mid+1
	return None

list=np.array([23,34,12,88,90,64,3,7,55])
sortedList=np.sort(list,kind='mergesort')
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