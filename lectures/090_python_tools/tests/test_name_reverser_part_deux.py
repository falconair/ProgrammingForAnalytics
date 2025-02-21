import pytest
from name_reverser import name_reverse_order

def test_name_reverse_order_normal():
    rslt = name_reverse_order("Michael Jordan")
    assert rslt == "Jordan, Michael"

    rslt = name_reverse_order("Lebron James")
    assert rslt == "James, Lebron"

def test_name_reverse_order_bad_inputs():

    # Empty string
    with pytest.raises(ValueError):
        rslt = name_reverse_order("")
        
