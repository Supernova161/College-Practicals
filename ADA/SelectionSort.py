import random
import time

def selection(list):
    
    for i in range(len(list)):
        min_inx = i 
        # list=[3,2,1] i=index 0 ,value 3 
        for j in range(i+1, len(list)):
        # j=(index=1, value=2 )
        # in second round j=(index=2, value=1)    
            if list[j] < list[min_inx]:
            #2<3
            #in second round 1<2 so min_inx =2 that is value=1    
                min_inx = j
                #now min_inx =1 that is value=2
        list[i], list[min_inx] = list[min_inx], list[i]

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

selection(list)

# Record the end time in microseconds
end_time = time.perf_counter()


print("Sorted list is: ", list)
execution_time = (end_time - start_time) * 1e6  # Convert to microseconds
print("Execution time:", execution_time,"microseconds")