import sys
import os

# grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
#
# sky_LR = [max(row) for row in grid]
# sky_UD = [max(col) for col in zip(*grid)]
#
# print sky_LR
# print sky_UD
#
# total = 0
#
# for j in range(len(grid)):
#     print len(grid)
#     for k in range(len(grid[0])):
#         # print sky_LR[j]
#         # print sky_UD[k]
#         total += min(sky_LR[j], sky_UD[k]) - grid[j][k]
#
# print total

# a = ['a','b','c','d']
#
# str = "".join(a)
#
# print str
#
# nums = [3,2,1,6,0,5]
#
# new_val = max(nums)
# split_index = nums.index(new_val)
# node = TreeNode(new_val)
#
# print nums[:split_index]
# print nums[split_index + 1:]

# if len(nums[:split_index]):
#     node.left=self.constructMaximumBinaryTree(nums[:split_index])
# if len(nums[split_index+1:]):
#     node.right=self.constructMaximumBinaryTree(nums[split_index+1:])




# list = ["1", "4", "0", "6", "9"]
#
# list.sort()
# print list


# list1 = [[]]*2
# print list1
#
# list1[0] = [3,'0']
# print list1
#
# list2 = list1.append(["append","append1"])
# print list1
#
#
# list1.extend(["extend","extend1"])
# print list1
#
# list1[4] = [99]
#
# print list1

# tup = ([1,2],'3',[])
# print tup
#
# tup[0].append(3)
# print tup
#
# tup[2].append('4')
# print(tup)
# del(tup)
# print(tup)





# def word_count(str):
#     counts = dict()
#     words = str.split(" ")
#
#     for word in words:
#         if word in counts:
#             counts[word] += 1
#         else:
#             counts[word] = 1
#
#     return counts
#
# print( word_count('the quick brown fox jumps over the lazy dog.'))
#
# import re
# for i in range(int(raw_input())):
#     print bool(re.search(r"^[+-]?\d*\.\d+$",raw_input().strip()))
#
# #Read input and assemble Phone Book
#
#
# n = int(input())
# phoneBook = {}
# for i in range(n):
#     contact = raw_input().split(' ')
#     phoneBook[contact[0]] = contact[1]
#
# print phoneBook


# # Process Queries
# lines = sys.stdin.readlines()
# for i in lines:
#     name = i.strip()
#     if name in phoneBook:
#         print(name + '=' + str( phoneBook[name] ))
#     else:
#         print('Not found')
#
# string = "abcabde"
#
# counts = {}
#
# for i in range(len(string)):
#     data = string[i]
#     if data in counts:
#         counts[data] +=1
#     else:
#         counts[data] = 1
#
# print counts
#

# print "Hello"


# # """
# # Given an array containing integers, zero is considered an invalid number
# #
# # and rest all other numbers are valid. If two nearest valid numbers are equal
# #
# # then double the value of the first one and make the second number as 0.
# #
# # At last move all the valid numbers on the left.
# #
# # Input:
# #
# # 2 4 5 0 0 5 5 4 8 6 0 6 8
# # Output:
# #
# # 2 4 10 5 4 8 12 8 0 0 0 0 0
# #
# #



# def sum_dublicate_item(list):
#     for i in range(len(list)):
#         if i < (len(list) - 2) and list[i] == list[i + 1]:
#             list[i] += list[i + 1]
#             list[i + 1] = 0
#
#     return list
#
#
# def shift_zero(list):
#     for i in range(len(list)):
#         if list[i] == 0 and (i < (len(list)) - 2) and list[i] == list[i + 1]:
#             for j in range(i + 1, len(list)):
#                 list[j - 1] = list[j]
#
#             list[len(list) - 1] = 0
#
#         if list[i] == 0:
#             for j in range(i + 1, len(list)):
#                 list[j - 1] = list[j]
#             list[len(list) - 1] = 0
#
#     return list
#
#
# list = [2, 4, 5, 0, 0, 5, 5, 4, 8, 6, 0, 6, 8]
#
# length = len(list)
#
# new_list1 = shift_zero(list)
# new_list2 = sum_dublicate_item(new_list1)
# new_list3 = shift_zero(new_list2)
#
# print new_list3

# import copy
#
# l1 = [1,2,3,4]
# l2 = l1
# print l1
# print l2
# print id(l1)
# print id(l2)
#
# l2.append(5)
# print(l1)
# print(l2)
#
#
# l3 = copy.copy(l1)
# print(l3)
# l3.append(11)
# print(l3)
# print(l1)
# print id(l3)
# print id(l1)
#
#
# l4 = copy.deepcopy(l2)
# print(l4)
# l4.append(12)
# print(l4)
# print(l2)
# print id(l4)
# print id(l2)


# import re
#
# url = "http://10.10.10.1/index.html"
#
# ipPattern = re.compile('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
# cms_ip_from_consul = re.findall(ipPattern, url)
#
# print cms_ip_from_consul
#
# wordsList = ['this', 'is', 'this', 'is', 'mine', 'this']
# wordDict = {}
#
# for item in wordsList:
#     if item not in wordDict:
#         wordDict[item] = 1
#     else:
#         wordDict[item] += 1
#
# print wordDict





