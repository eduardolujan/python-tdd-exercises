#
# http://codekata.com/kata/kata02-karate-chop/
#


def chop(target: int, elements: list[int]) -> int:
    """
    :param target: the integer to search into elements array
    :param elements: ordered list of elements

    :return: -1 if element not found or the index of the first occurrence
    """
    if not elements:
        return -1
    try:
        return elements.index(target)
    except ValueError:
        return -1
