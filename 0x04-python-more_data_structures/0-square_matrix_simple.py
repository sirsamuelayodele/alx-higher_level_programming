#!/usr/bin/python3
def sqr(element):
    if isinstance(element, list):
        return list(map(sqr, element))
    return (element * element)


def square_matrix_simple(matrix=[]):
    return list(map(sqr, matrix))
