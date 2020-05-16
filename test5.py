import sys
import os


# def is_anagram(data1, data2):
#     Flag = True
#     if len(data1)  != len(data2):
#         print "Not an anagram"
#     else:
#         for char in data1:
#             if char not in data2:
#                 Flag = False
#                 break
#             else:
#                 data2 = data2.replace(char,"",1)
#
#
#         if Flag == True:
#             print "Input strings are anagram"
#         else:
#             print "Input strings are not an anagram"


def is_anagram(data1, data2):
    dic_data1, dic_data2 = {}, {}
    for i in data1:
        dic_data1[i] = dic_data1.get(i,0) + 1

    for i in data2:
        dic_data2[i] = dic_data2.get(i,0) + 1

    print dic_data2
    print dic_data1

    if dic_data1 == dic_data2:
        print "Input strings are anagram"
    else:
        print "Input strings are not an anagram"


if __name__ == "__main__":
    string1 = str(raw_input())
    string2 = str(raw_input())
    is_anagram(string1, string2)
