import random
import time

def insertion(list):
    for i in range(1, len(list)):
        #list=[17, 89, 3, 38, 32] current value=89, i=1
        #2  #current value = 3, i=2
        current_value = list[i]
        index = i-1 #previous value = 17 , index = 0
                    #2    #previous value = 89 , index =1
        while index >= 0: #0>=0  #2 1>=0
            if current_value < list[index]:    #89<17 False   
                                               #2   3<89
                list[index+1], list[index] = list[index], list[index+1]  #list[index+1], list[index] =  89, 3
                index -= 1   #2 index=0
            else:
                break



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

insertion(list)

# Record the end time in microseconds
end_time = time.perf_counter()


print("Sorted list is: ", list)
execution_time = (end_time - start_time) * 1e6  # Convert to microseconds
print("Execution time:", execution_time,"microseconds")