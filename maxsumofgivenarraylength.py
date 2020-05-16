

def maxSumSubArray (num, k):
    maxsum = 0
    currentsum = 0
    for i in range(len(num)):
        currentsum += num[i]
        if (i >= k-1):
            maxsum = max(maxsum, currentsum)
            currentsum -= num[i - (k - 1)]

    print ("I am going great")

    return maxsum



a = [2,1,5,7,2,0,7,3]
k = 3

print(maxSumSubArray(a , k))