import time

pos = 0
def search(list, n):
    l = 0
    u = len(list)-1

    while l <= u:
        mid = (l+u) // 2

        if list[mid] == n:
            globals()['pos'] = mid+1
            return True
        else:
            if list[mid] < n:
                l = mid+1
            else:
                u = mid-1


list = [26,34,65,77,88,91]
n = 65

# Record the start time in microseconds
start_time = time.perf_counter()

if search(list, n):
    print("Found at",pos)
else:
    print("Not Found")

# Record the end time in microseconds
end_time = time.perf_counter()

execution_time = (end_time - start_time) * 1e6  # Convert to microseconds
print("Execution time:", execution_time,"microseconds")
