import pytest

from pandas.dataframe import DataFrame

def test_dataframe_creation_error():
    with pytest.raises(ValueError):
        df_error = DataFrame({})

def test_dataframe_creation_valid():
    valid_dict = {
        "A": [1,2,3,4],
        "B": [1,2,3,4]
    }
    df_valid = DataFrame(valid_dict)

    assert df_valid.data == valid_dict



