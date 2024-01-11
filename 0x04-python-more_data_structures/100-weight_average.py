#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    wt_sum = 0
    avg = 0
    for i, j in my_list:
        avg += i * j
        wt_sum += j
    return avg / wt_sum
