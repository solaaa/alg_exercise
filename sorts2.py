# 1. counting sort
# eg. 1~100
def counting_sort(arr):
    n = 100
    count = [0] * n
    for i in range(len(arr)):
        count[arr[i]] += 1
    arr = []
    for i in range(n):
        while count[i] > 0:
            count[i] -= 1
            arr.append(i)
    return arr
#print(counting_sort([1,4,2,88,44,77,4,33,88,3,5,6,77,44,6,22,8]))

# 2. Cardinality sort
# eg. 0~999
def cardinality_sort(arr):
    count = []
    for _ in range(10):
        count.append([])
    epoch = 3
    for i in range(epoch):
        for j in range(len(arr)):
            count[(arr[j]//(10**i))%10].insert(0, arr[j])
            
        arr = []
        
        for k in range(10):
            while count[k] != []:
                arr.append(count[k].pop())
    return arr
#print(cardinality_sort([171,41,241,488,414,771,33,334,886,321,545,31,774,445,611,242,841]))     

# 3. heap sort
def heap_sort(arr):
    r = len(arr) - 1
    for i in range(len(arr)-1):
        k = len(arr[:r])//2 - 1
        while k >= 0:
            if 2*k + 2 > r:
                if arr[k] < arr[2*k + 1]:
                    t = arr[k]
                    arr[k] = arr[2*k + 1]
                    arr[2*k + 1] = t
            else:
                if arr[k] < arr[2*k + 1] and arr[2*k + 2] < arr[2*k + 1]:
                    t = arr[k]
                    arr[k] = arr[2*k + 1]
                    arr[2*k + 1] = t 
                elif arr[k] < arr[2*k + 2] and arr[2*k + 1] < arr[2*k + 2]:
                    t = arr[k]
                    arr[k] = arr[2*k + 2]
                    arr[2*k + 2] = t  
                else:
                    pass
            k -= 1
        t = arr[0]
        arr[0] = arr[r]
        arr[r] = t
        r -= 1
    return arr
print(heap_sort([171,41,241,488,414,771,33,334,886,321,545,31,774,445,611,242,841]))     