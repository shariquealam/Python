#!/bin/python

from __future__ import print_function

import os
import sys


#
# Complete the timeConversion function below.
#
def timeConversion(s):
    print(s)
    result = ""
    if "PM" in s.upper():
        time_adder = 0
        s = s.split(':')
        if s[0] == "12":
            time_adder = 0
        else:
            time_adder = 12
        result = ((str(int(s[0]) + time_adder) + ":" + str(s[1]) + ":" + str(s[2])).upper()).replace("PM", "")
    elif "AM" in s.upper():
        s = s.split(':')
        if s[0] == "12":
            result = (("00" + ":" + str(s[1]) + ":" + str(s[2])).upper()).replace("AM", "")
        else:
            if len(s[0]) == 1:
                s[0] = "0" + s[0]
            result = ((str(s[0]) + ":" + str(s[1]) + ":" + str(s[2])).upper()).replace("AM", "")

    print(result)

    return result


if __name__ == '__main__':
    s = raw_input()

    result = timeConversion(s)
    print (result)
