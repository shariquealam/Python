#!/bin/python

#from __builtins__ import hash
import sys
import os

#!/bin/python

import sys

# hexVal = "AB89"
# len = len(hexVal)
# print len
# base = 1
# dec_val = 0
# i = len-1
#
# while i >= 0:
#     if ((hexVal[i]) >= '0' and (hexVal[i]) <= '9'):
#         dec_val += (ord(hexVal[i]) - 48) * base
#         base = base * 16
#     elif ((hexVal[i]) >= 'A' and (hexVal[i]) <= 'F'):
#         dec_val += (ord(hexVal[i]) - 55) * base
#         base = base * 16
#     else:
#         print "Invalid input"
#         break
#
#     i = i-1
#
#
# print dec_val

#
# if __name__ == "__main__":
#         s = raw_input()
#         keypad = raw_input()
#         #res = entryTime(s, keypad)

import re

# string_with_newlines = """something
# someotherthing"""
#
# print re.match('some', string_with_newlines) # matches
# print re.match('someother',
#                string_with_newlines) # won't match
# print re.match('^someother', string_with_newlines,
#                re.MULTILINE) # also won't match
# print re.search('someother',
#                 string_with_newlines) # finds something
# print re.search('^someother', string_with_newlines,
#                 re.MULTILINE) # also finds something
#
# m = re.compile('thing$', re.MULTILINE)
#
# print m.match(string_with_newlines) # no match
# print m.match(string_with_newlines, pos=4) # matches
# print m.search(string_with_newlines,
#                re.MULTILINE) # alsolso matches


# # Compile regular expression
# obj = re.compile('hi', re.M)
# # Use the object to match
# mat = obj.match('hi how are you?')
# print(mat)
#
# # Do the match directly using re.match
# mat = re.match('hi', 'hi how are you?', re.M)
# print(mat)

# nterms = 10
#
# def fib(n):
#     if (n <= 1):
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
#
# for i in range(nterms):
#        print(fib(i))



# def findAnagrams(s, p):
#         """
#         :type s: str
#         :type p: str
#         :rtype: List[int]
#         """
#         result = []
#         dic_p, dic_s = {}, {}
#         n_p, n_s = len(p), len(s)
#         if n_s < n_p:
#             return result
#         for char in p:
#             dic_p[char] = dic_p.get(char, 0) + 1
#         list_chars = dic_p.keys() #list of characters in p that we care about
#         for char in list_chars:
#             dic_s[char] = 0 # Making an empty dictionary for keeping track of s
#         for i in range(n_p): # Initiation of dic_s
#             if s[i] in list_chars:
#                 dic_s[s[i]] += 1
#         if dic_s == dic_p:
#             result.append(0)
#         for i in range(n_p, n_s):
#             if s[i] in list_chars:# adding the new element
#                 dic_s[s[i]] += 1
#             if s[i - n_p] in list_chars:# removing the oldest element
#                 dic_s[s[i - n_p]] -= 1
#             if dic_s == dic_p: # Checking to see if we have anagram
#                 result.append(i - n_p + 1)
#         return(result)
#
#
# print findAnagrams("cbaababacd","abc")


# Program to find the numbers of line required to print the given string.
# In each line 100 size character can be print.
# def numberOfLines(widths, S):
#     totalLines = 0
#     curWidth = 0
#     for i in S:
#         idx = ord(i) - 97
#         w = widths[idx]
#         if curWidth + w > 100:
#             totalLines += 1
#             curWidth = 0
#         curWidth += w
#
#     return [totalLines + 1, curWidth]
#
#
# widths = [7,5,4,7,10,7,9,4,8,9,6,5,4,2,3,10,9,9,3,7,5,2,9,4,8,9]
# S = "zlrovckbgjqofmdzqetflraziyvkvcxzahzuuveypqxmjbwrjvmpdxjuhqyktuwjvmbeswxuznumazgxvitdrzxmqzhaaudztgie"
#
# print numberOfLines(widths, S)


# list1 = ['spam', 'ham', 'eggs']
# list2 = ['a', 'b', 3]
#
# list3 =  list(zip(list1, list2))
#
# print list3
#
# list3[0] = 4
#
# print list3
#
#
# for i,j in zip(list1, list2):
#     print i
#     print j


# numberList = [1, 2, 3]
# strList = ['one', 'two', 'three']
#
# # No iterables are passed
# result = zip()
#
# # Converting itertor to list
# resultList = list(result)
# print(resultList)
#
# # Two iterables are passed
# result1 = zip(numberList, strList)
#
# print list(result1)
#
# # Converting itertor to set
# resultSet = set(result)
# print(resultSet)


# numbersList = [1, 2, 3]
# strList = ['one', 'two']
# numbersTuple = ('ONE', 'TWO', 'THREE', 'FOUR')
#
# result = zip(numbersList, numbersTuple)
#
# # Converting to set
# resultSet = set(result)
# print(resultSet)
# print result
#
# result = zip(numbersList, strList, numbersTuple)
#
# # Converting to set
# resultSet = set(result)
# print(resultSet)
# print result