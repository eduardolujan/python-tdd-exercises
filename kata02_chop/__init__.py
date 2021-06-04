def chop(target: int, elements: list[int]) -> int:
    if not elements:
        return -1
    try:
        return elements.index(target)
    except ValueError:
        return -1
