#
# def longestOnes(A, K):
#     start = 0
#     end = 0
#     res = 0
#     zero_count = 0
#     while end < len(A):
#         if A[end] == 1:
#             end += 1
#             res = max(res, end - start)
#         else:
#             if zero_count < K:
#                 end += 1
#                 zero_count += 1
#                 res = max(res, end - start)
#             else:
#                 while start <= end and zero_count >= K:
#                     if A[start] == 0:
#                         zero_count -= 1
#                     start += 1
#     return res
#
# print(longestOnes([1,1,1,0,0,0,1,1,1,1,0] , 2))

for i in range(3,4):
    print (i)