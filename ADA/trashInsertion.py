# Insertion Sort
def sort(list):
    for i in range(1,len(list)):
        current_element = list[i]
        index = i-1
        while current_element < list[index] and index>=0:
            list[index],list[index+1] = list[index+1],list[index]
            index = index-1
        # list[index+1] = current_element


list = [25,68,96,74,12,5,36,78,100,18,1,56,23]
print(list)
sort(list)
print(list)
