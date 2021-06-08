#
# http://codekata.com/kata/kata02-karate-chop/
#
from typing import List


def order_arrays(elements: List[int]) -> List[int]:
    n = len(elements)
    for i in range(n):
        for j in range(0, n - 1):
            if elements[j] > elements[j + 1]:
                elements[j], elements[j + 1] = elements[j + 1], elements[j]
    return elements


def chop(target: int, elements: List[int], index: int = 0) -> int:
    elements = order_arrays(elements)
    for pos, element in enumerate(elements):
        if target == element:
            return pos
    return -1
