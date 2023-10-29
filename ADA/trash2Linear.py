# Linear Search
def search(list,n):
    for i in list:
        if i == n:
            return True
    else:
        return False




list = [1,2,3,5,6,7,10]
n = 7

if search(list,n):
    print("Found")
else:
    print("Not found")
    