import pytest

from . import CollectionFilter
from . import TempCollection
from . import TempRecord


@pytest.fixture()
def elements():
    return TempCollection()


def test_basic_objects_structure(elements):
    assert len(elements) == 0


def test_add_temp_record(elements):
    temp_record = TempRecord(dy=1, mxt=88, mnt=59)
    elements.append(temp_record)
    assert len(elements) == 1


def test_add_temp_record_invalid_obj(elements):
    with pytest.raises(ValueError):
        elements.append(None)


def test_basic_filter_interface(elements):
    elements.append(TempRecord(dy=1, mxt=88, mnt=59))
    filtered_elements = CollectionFilter(elements).max()
    assert isinstance(filtered_elements, TempCollection)
    assert len(filtered_elements) == 1
