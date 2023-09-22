import random
import time

def binary_search(arr, target):
    comparisons = 0
    left, right = 0, len(arr) - 1
    while left <= right:
        comparisons += 1
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1, comparisons

def analyze_binary_search(arr, target):
    # Best Case: The element is at the middle of the list.
    start_time = time.perf_counter()
    result, comparisons = binary_search(arr, arr[len(arr) // 2])
    end_time = time.perf_counter()
    best_case_time = (end_time - start_time) * 1e6  

    # Worst Case: The element is not in the list.
    start_time = time.perf_counter()
    result, comparisons = binary_search(arr, target)
    end_time = time.perf_counter()
    worst_case_time = (end_time - start_time) * 1e6  

    # Average Case: The element is at a random position.
    random.shuffle(arr)
    start_time = time.perf_counter()
    result, comparisons = binary_search(arr, target)
    end_time = time.perf_counter()
    average_case_time = (end_time - start_time) * 1e6  

    return best_case_time, worst_case_time, average_case_time, comparisons

# Define the size of the list and the target element.
list_size = 100000
target_element = random.randint(0, list_size - 1)

# Create a sorted list of integers.
sorted_list = list(range(list_size))

best_case_time, worst_case_time, average_case_time, comparisons = analyze_binary_search(sorted_list, target_element)

print(f"List size: {list_size}")
print(f"Target element: {target_element}")
print(f"Best Case Time: {best_case_time:.6f} ")
print(f"Worst Case Time: {worst_case_time:.6f} ")
print(f"Average Case Time: {average_case_time:.6f} ")
print(f"Total Comparisons: {comparisons}")
