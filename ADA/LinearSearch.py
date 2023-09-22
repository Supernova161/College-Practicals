import time

pos = 0
def search(list, n):
    for i in list:
        globals()['pos'] += 1
        if i == n:
            return True
    return False

list = []
for i in range(1,1000):
    # num = int(input("Enter a number: "))
    num = i
    list.append(num)
    i += 1
print("Your list is:   ", list)
n = 10


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
