import random
import time

def merge_sort(list):
    if len(list) > 1:
        left_list = list[:len(list)//2]
        right_list = list[len(list)//2:]

        merge_sort(left_list)
        merge_sort(right_list)

        i=0
        j=0
        k=0

        while i<len(left_list) and j<len(right_list):
            if left_list[i] < right_list[j]:
                list[k] = left_list[i]
                i += 1
                k += 1
            else:
                list[k] = right_list[j]
                j += 1
                k += 1

        while i<len(left_list):
                list[k] = left_list[i]
                i += 1
                k += 1

        while j<len(right_list):
                list[k] = right_list[j]
                j += 1
                k += 1     

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

merge_sort(list)

# Record the end time in microseconds
end_time = time.perf_counter()


print("Sorted list is: ", list)
execution_time = (end_time - start_time) * 1e6  # Convert to microseconds
print("Execution time:", execution_time,"microseconds")                 