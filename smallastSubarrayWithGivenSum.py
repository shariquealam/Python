
import sys

def smallastSubarrayWithGivenSum (num, sum):
    minSubArray = sys.maxsize
    print(minSubArray)
    currentsum = 0
    arrayStart = 0

    for arrayend in range(len(num)):
        currentsum += num[arrayend]

        while currentsum >= sum :
            minSubArray = min(minSubArray, (arrayend - arrayStart + 1))
            currentsum -= num[arrayStart]
            arrayStart += 1

    return minSubArray



a = [2,1,5,7,2,0,7,3]
k = 6

print(smallastSubarrayWithGivenSum(a , k))