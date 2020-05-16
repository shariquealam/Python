
def maxSatisfied (customers, grumpy, X):
    totalSatisfyCustomer = 0
    maxGrumpy = 0
    maxCustomerSum = 0
    currentCustomerSum = 0
    currentGrumpy = 0
    startIndex = 0
    endIndex = 0

    for arrayEnd in range(len(customers)):
        currentCustomerSum += customers[arrayEnd]
        currentGrumpy += grumpy[arrayEnd]
        if arrayEnd >= (X - 1):
            if currentGrumpy >= maxGrumpy :
                maxGrumpy = currentGrumpy
                if maxCustomerSum < currentCustomerSum:
                    maxCustomerSum = currentCustomerSum
                    endIndex = arrayEnd
                    startIndex = arrayEnd - (X-1)
                currentCustomerSum -= customers[arrayEnd - (X - 1)]
                currentGrumpy -= grumpy[arrayEnd - (X - 1)]
            else:
                currentCustomerSum -= customers[arrayEnd - (X - 1)]
                currentGrumpy -= grumpy[arrayEnd - (X - 1)]


    totalSatisfyCustomer += maxCustomerSum

    print(startIndex)
    print(endIndex)
    print(totalSatisfyCustomer)

    for i in range(startIndex):
        if grumpy[i] == 0:
            totalSatisfyCustomer += customers[i]

    for i in range((endIndex+1), arrayEnd+1):
        if grumpy[i] == 0:
            totalSatisfyCustomer += customers[i]

    return totalSatisfyCustomer


# C = [9,10,4,5]
# G = [1,0,1,1]
# X = 1

# C = [7,8,8,6]
# G = [0,1,0,1]
# X = 3

C = [1,0,1,2,1,1,7,5]
G = [0,1,0,1,0,1,0,1]
X = 3

# C = [4,10,10]
# G = [1,1,0]
# X = 2

print(maxSatisfied(C , G, X))