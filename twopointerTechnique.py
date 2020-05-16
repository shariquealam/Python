import re

# def moveZeroes(nums):
#     """
#     Do not return anything, modify nums in-place instead.
#     """
#     nums.sort()
#     print(nums)
#     start, end = 0, 0
#     while end < len(nums):
#         if nums[end] != 0:
#             nums[start], nums[end] = nums[end], nums[start]
#
#         if nums[start] != 0:
#             start += 1
#         end += 1
#
#     return nums
#
#
# a = [0,2,-1,4,5,0,0,5]
# # a = [0,1,0,3,12]
# # a = [1]
# print(moveZeroes(a))


# def twoSum( numbers, target):
#     R = []
#     start, end = 0, (len(numbers) - 1)
#     while start < end:
#         if ((numbers[start] + numbers[end]) == target):
#             R.append(start)
#             R.append(end)
#             break;
#         elif ((numbers[start] + numbers[end]) < target):
#             start += 1
#         else:
#             end -= 1
#     print(R)
#     return R
#
# a = [2,7,11,15]
# target = 9
# print(twoSum(a, target))


# def reverseVowels(s):
#     V = ['a', 'e', 'i', 'o', 'u']
#     start, end = 0, len(s) - 1
#     s = list(s)
#     while start < end:
#         if ((s[start].lower() in V) and (s[end].lower() in V)):
#             s[start], s[end] = s[end], s[start]
#             start += 1
#             end -= 1
#
#         if (s[end] not in V):
#             end -= 1
#
#         if (s[start] not in V):
#             start += 1
#
#     return "".join(s)
#
#
# a = "aA"
# print(reverseVowels(a))


def isPalindrome(s):
    flag = True
    newStr = re.sub('[^A-Za-z0-9]+', '', s)
    print (newStr)
    start, end = 0, len(newStr) - 1
    while start < end:
        if newStr[start].lower() != newStr[end].lower():
            flag = False
            break;
        else:
            start += 1
            end -= 1
    return flag



a = "A man, a plan, a canal: Panama"
print(isPalindrome(a))







