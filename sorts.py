# 1. bubble sort
def bubble_sort(arr):
    arr_len = len(arr)
    for k in range(arr_len-1):
        for i in range(arr_len-1-k):
            if arr[i] > arr[i+1]:
                t = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = t
    return arr

#print(bubble_sort([4,2,6,8,3,5,77]))

# 2. selection sort
def my_min(arr):
    val = arr[0]
    argmin = 0
    for i in range(1, len(arr)):
        if val > arr[i]:
            val = arr[i]
            argmin = i
    return val, argmin
def selection_sort(arr):
    arr_len = len(arr)
    for i in range(arr_len-1):
        cur_min, cur_index = my_min(arr[i:])
        cur_index += i
        t = arr[i]
        arr[i] = cur_min
        arr[cur_index] = t
    return arr
#print(selection_sort([4,2,6,8,3,5,77,1]))

# 3. Insertion sort
def insertion_sort(arr):
    arr_len = len(arr)
    
    for i in range(1, arr_len):
        j = i
        while j > 0 and arr[j] < arr[j-1]:
            t = arr[j]
            arr[j] = arr[j-1]
            arr[j-1] = t
            j -= 1
    return arr
#print(insertion_sort([4,2,6,8,3,5,77,1]))

# 4. merging sort
def merging_sort(arr):
    if len(arr) == 1:
        return arr
    l = merging_sort(arr[0:len(arr)//2])
    r = merging_sort(arr[len(arr)//2:])
    m = [0] * (len(l) + len(r))
    s, t = 0, 0
    for i in range(len(m)):
        if s<len(l) and t<len(r):
            if l[s] < r[t]:
                m[i] = l[s]
                s += 1
            else:
                m[i] = r[t]
                t += 1
        elif s==len(l) and t<len(r):
            m[i] = r[t]
            t += 1
        else:
            m[i] = l[s]
            s += 1
    return m
#print(merging_sort([4,2,6,8,3,5,77,1]))

# 5. quick sort
def partition(arr, l, r):
    if l>=r:
        return arr
    i = l-1
    j = l
    while j < r:
        if arr[j] < arr[r]:
            i += 1
            t = arr[i]
            arr[i] = arr[j]
            arr[j] = t
        j += 1
    i += 1
    t = arr[i]
    arr[i] = arr[r]
    arr[r] = t
    
    arr = partition(arr, l, i-1)
    arr = partition(arr, i+1, r)
    return arr
def qsort(arr):
    arr = partition(arr, 0, len(arr)-1)
    return arr
#print(qsort([4,2,6,8,3,5,77,1]))

# 6. shell sort
def shell_sort(arr, step = 3):
    while step > 0:
        i = step
        while i < len(arr):
            k = i
            while k - step >= 0:
                if arr[k] > arr[k-step]:
                    break
                t = arr[k]
                arr[k] = arr[k-step]
                arr[k-step] = t
                k -= step
            i += 1
        step -= 1
    return arr
#print(shell_sort([6,5,3,1,8,7,2,4]))

# 7. heap sort
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
#print(heap_sort([171,41,241,488,414,771,33,334,886,321,545,31,774,445,611,242,841]))

# 8. counting sort
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

# 9. Cardinality sort
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

     
