from kata02_chop import chop


def test_empty_array():
    assert -1 == chop(3, [])


def test_target_not_found():
    assert -1 == chop(3, [1])


def test_found_target_simple():
    assert 0 == chop(1, [1])


def test_found_target_two_elements():
    assert 0 == chop(1, [1, 2])
    assert 1 == chop(2, [1, 2])


def test_not_found_target_two_elements():
    assert -1 == chop(0, [1, 2])
    assert -1 == chop(3, [1, 2])


def test_found_element_full_array():
    assert 0 == chop(1, [1, 3, 5])
    assert 1 == chop(3, [1, 3, 5])
    assert 2 == chop(5, [1, 3, 5])
    assert 0 == chop(1, [1, 3, 5, 7])
    assert 1 == chop(3, [1, 3, 5, 7])
    assert 2 == chop(5, [1, 3, 5, 7])
    assert 3 == chop(7, [1, 3, 5, 7])


def test_not_found_full_array():
    assert -1 == chop(0, [1, 3, 5])
    assert -1 == chop(2, [1, 3, 5])
    assert -1 == chop(4, [1, 3, 5])
    assert -1 == chop(6, [1, 3, 5])
    assert -1 == chop(0, [1, 3, 5, 7])
    assert -1 == chop(2, [1, 3, 5, 7])
    assert -1 == chop(4, [1, 3, 5, 7])
    assert -1 == chop(6, [1, 3, 5, 7])
    assert -1 == chop(8, [1, 3, 5, 7])


def test_not_found_in_not_sorted_array():
    assert -1 == chop(2, [1, 3, 2, 4])
