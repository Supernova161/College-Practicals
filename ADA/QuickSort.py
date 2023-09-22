import random
import time

# Quick sort in Python

# function to find the partition position
def partition(array, low, high):

  # choose the rightmost element as pivot
  pivot = array[high]

  # pointer for greater element
  i = low - 1

  # traverse through all elements
  # compare each element with pivot
  for j in range(low, high):
    if array[j] <= pivot:
      # if element smaller than pivot is found
      # swap it with the greater element pointed by i
      i = i + 1

      # swapping element at i with element at j
      (array[i], array[j]) = (array[j], array[i])

  # swap the pivot element with the greater element specified by i
  (array[i + 1], array[high]) = (array[high], array[i + 1])

  # return the position from where partition is done
  return i + 1

# function to perform quicksort
def quickSort(array, low, high):
  if low < high:

    # find pivot element such that
    # element smaller than pivot are on the left
    # element greater than pivot are on the right
    pi = partition(array, low, high)

    # recursive call on the left of pivot
    quickSort(array, low, pi - 1)

    # recursive call on the right of pivot
    quickSort(array, pi + 1, high)


# list = [12,45,6,13,100,67]
list = []
n = int(input("Enter how many numbers you want: "))
for i in range(n):
    # num = int(input("Enter a number: "))
    num = random.randint(0, 100000)
    list.append(num)
print("Your list is:   ", list)
size = len(list)

 
# Record the start time in microseconds
start_time = time.perf_counter()

quickSort(list, 0, size - 1)

# Record the end time in microseconds
end_time = time.perf_counter()


print("Sorted list is: ", list)
execution_time = (end_time - start_time) * 1e6  # Convert to microseconds
print("Execution time:", execution_time,"microseconds")