import time

def recursive(n):
    if n == 0:
        return 1
    else:
        fact =  n * recursive(n-1)
    return fact

start_time = time.perf_counter()

print(recursive(5))

end_time = time.perf_counter()

execution_time = (end_time - start_time) * 1e6  # Convert to microseconds
print("Execution time:", execution_time,"microseconds")