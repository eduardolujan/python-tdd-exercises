#
# http://codekata.com/kata/kata02-karate-chop/
#


def chop(target: int, elements: list[int], index: int = 0) -> int:
    """
    :param target: the integer to search into elements array
    :param elements: ordered list of elements
    :param index: processing index element

    :return: -1 if element not found or the index of the first occurrence
    """
    if not elements:
        return -1
    if len(elements) == 1:
        if elements[0] != target:
            return -1
        else:
            return index

    if len(elements) == 2:
        if elements[0] == target:
            return index
        elif elements[1] == target:
            return index + 1
        return -1

    elements_count = len(elements)
    center = elements_count // 2
    first_half = chop(target, elements[0:center], index)
    if first_half < 0:
        second_half = chop(target, elements[center:elements_count], center)
        if second_half < 0:
            return -1
        else:
            return second_half
    else:
        return first_half
