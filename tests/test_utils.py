import pytest
from src.utils import get_data_from_xlsx

def test_get_data_from_xlsx():
    result = get_data_from_xlsx('../data/operations.xls')
    assert len(result) > 0
