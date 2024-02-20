# left side se funk marte hain, adjacent se compare swape hote hote, right side me bada bubble (element) nikal jata hai

# 1st for loop is just for iteration purpose
# 2nd for does actual sorting by adjacent comparing amd swapping
# in between, right part will be sorted
def bubble_sort(arr):
    n=len(arr)
    for i in range(n-1):
        for j in range(n-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

print(bubble_sort([3,5,1,2,7,2]))





# consider left part as sorted and right part as unsorted
# in right part, consider 1st element is smallest
# now find minimum element in unsorted part(right part) and swap with 1st element in unsorted part
# in between left part will be sorted
def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        #from ith index, our array is unsorted 
        curr_min=arr[i] # consider 1st element as minimum
        min_idx = i
        for j in range(i,n):
            if arr[j]<curr_min:
                curr_min=arr[j]
                min_idx=j
        arr[i],arr[min_idx] = arr[min_idx],arr[i]
    return arr
print(selection_sort([3,5,1,2,7,2]))


def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(i,n):
            if arr[j] < arr[i]:
                arr[j],arr[i] = arr[i],arr[j]
    return arr



print(selection_sort([3,5,1,2,7,2]))

def insertion_sort(arr):
    pass
