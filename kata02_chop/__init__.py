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
    last = None
    for key, value in enumerate(elements):
        if last and last > value:
            return -1
        if value == target:
            return key
        last = value
    return -1
