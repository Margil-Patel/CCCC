def nextGE(arr):
    n = len(arr)
    nge = [-1] * n
    for i in range(n):
        for j in range(i+1,n):
            if arr[j] > arr[i]:
                nge[i] = arr[j]
                break
    
    return nge



arr = [4,5,2,10,8]

print("NGE", nextGE(arr))