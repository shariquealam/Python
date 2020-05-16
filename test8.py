import os

fd = "Commands1.txt"

# popen() is similar to open()
# file = open(fd, 'w')
# file.write("Hello")
# file.close()
# file = open(fd, 'r')
# text = file.read()
# print(text)

# popen() provides a pipe/gateway and accesses the file directly
# file = os.popen(fd, 'w')
# file.write("Hello")
#
# file1 = os.popen(fd, 'r')
# print file1.read()
# os.close(file1)
# File not closed, shown in next function.

# os.rename(fd,'New.txt')
# os.rename(fd,'New.txt')


# noprimes = [j for i in range(2, 8) for j in range(i*2, 50, i)]
# primes = [x for x in range(2, 50) if x not in noprimes]
# print (noprimes)
# print (primes)

# def decompressRLElist(nums):
#     L = []
#     for i in range(0,len(nums),2):
#         v = nums[i + 1]
#         for j in range(nums[i]):
#             L.append(v)
#
#     print(L)
#
# print(decompressRLElist([1,2,3,4]))

# def smallerNumbersThanCurrent(nums):
#     sorted_list = sorted(nums)
#     return [sorted_list.index(x) for x in nums]
#
# print(smallerNumbersThanCurrent([8,1,2,2,3]))

a = [1,1,1,0,0,0,0,1,1,1,1,0]
print(a[1::])