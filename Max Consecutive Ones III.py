

def maxConsecutiveOnes(num , k):
    maxSubArray = 0
    currentCount = 0
    arrayStart = 0

    for arrayEnd in range(len(num)):
        if num[arrayEnd] == 0:
            if currentCount < k:
                maxSubArray = max(maxSubArray, (arrayEnd - arrayStart) + 1)
                currentCount += 1
            else:
                while num[arrayStart] != 0:
                    arrayStart += 1
                arrayStart += 1
        else:
            maxSubArray = max(maxSubArray, (arrayEnd - arrayStart) + 1)

    return maxSubArray

a = [1,1,1,0,0,0,1,1,1,1,0]
k = 2


print(maxConsecutiveOnes(a, k))