#!/usr/bin/python3
def uniq_add(my_list=[]):
    new = set(my_list)
    fsum = 0
    for i in new:
        fsum += i
    return (fsum)
