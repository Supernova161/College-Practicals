import time

def iterative(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    return fact

start_time = time.perf_counter()

print(iterative(5))

end_time = time.perf_counter()

execution_time = (end_time - start_time) * 1e6  # Convert to microseconds
print("Execution time:", execution_time,"microseconds")