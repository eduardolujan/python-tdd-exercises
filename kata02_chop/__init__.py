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

    if elements[0] == target:
        return index
    if elements[-1] == target:
        return len(elements) - 1

    elements_count = len(elements)
    center = elements_count // 2

    if target <= elements[center - 1]:
        return chop(target, elements[0:center], index)
    if target >= elements[center]:
        return chop(target, elements[center:elements_count], center)
    return -1
