def binary_search(l,target,low=None,high=None):
    if low == None:
        low = 0
    if high == None:
        high = len(l)-1
    
    midpoint = (low+high) //2

    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint]:
        return binary_search(l,target,low,midpoint-1)
    else:
        return binary_search(l, target, midpoint+1, high)


l = [1,2,3,4,5,6,7,8,9]
target = 6
print(binary_search(l,target))