import random
import time

def heapify(list, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and list[left] > list[largest]:
        largest = left

    if right < n and list[right] > list[largest]:
        largest = right

    if largest != i:
        list[i], list[largest] = list[largest], list[i]
        heapify(list, n, largest)

def heap_sort(list):
    n = len(list)

    # Build a max-heap.
    for i in range(n // 2 - 1, -1, -1):
        heapify(list, n, i)

    # Extract elements from the heap one by one.
    for i in range(n - 1, 0, -1):
        list[i], list[0] = list[0], list[i]  # Swap the maximum element with the last element.
        heapify(list, i, 0)  # Call heapify on the reduced heap.

# list = [12,45,6,13,100,67]
list = []
n = int(input("Enter how many numbers you want: "))
for i in range(n):
    # num = int(input("Enter a number: "))
    num = random.randint(0, 100000)
    list.append(num)
print("Your list is:   ", list)


# Record the start time in microseconds
start_time = time.perf_counter()

heap_sort(list)

# Record the end time in microseconds
end_time = time.perf_counter()


print("Sorted list is: ", list)
execution_time = (end_time - start_time) * 1e6  # Convert to microseconds
print("Execution time:", execution_time,"microseconds")
