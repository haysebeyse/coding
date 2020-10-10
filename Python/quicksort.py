'''
Quicksort algorithm uses D&C (Divide and Conquer):
  1. Figure out base case. Simplest possible case.
  2. Divide/decrease problem until it becomes base case. 

Algorithm O(n log n):
  1. Pick first item in array which is called pivot.
  Note: Pivot could be any element and can be selected randomly as well.
  2. Partition the array by seperating items less <= pivot and items greater > pivot.
  Note: Imagine pivot in the middle while less on left and greater on right.
  3. Keep partioning until base case (1 item array) is reached.
'''
def quicksort(array):
  if len(array) < 2:
    return array
  else:
    pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    print(str(less) + " < " + str(pivot))
    greater = [i for i in array[1:] if i > pivot]
    print(str(greater) + " > " + str(pivot))
    print("\n")
    return quicksort(less) + [pivot] + quicksort(greater)
    

print(quicksort([10, 5, 2, 3, 4, 4, 0, 8, 1, 9, 9]))
