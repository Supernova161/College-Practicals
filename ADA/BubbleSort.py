import random
import time

def bubble(list):
    size = len(list)

    # size-1 is done because the range is started from 0
    for i in range(size - 1):
        # size-1-i as we have to left out last element as it's already sorted
        # as [5,3,1] i=0,size=3 so range will be  3-1-0=2 so it will swap to 3 elements only 
        # as i will be increase the traversing will be decrease
        # in second loop of i will be i=1 so range 3-1-1=1 so it will swap to 2 elements only
        for j in range(size-1-i):
            if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
            
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

bubble(list)

# Record the end time in microseconds
end_time = time.perf_counter()


print("Sorted list is: ", list)
execution_time = (end_time - start_time) * 1e6  # Convert to microseconds
print("Execution time:", execution_time,"microseconds")