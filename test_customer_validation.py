import pytest
from customer_validation import validate_customer


@pytest.mark.parametrize("customer_id, customer_name, age, expected", [
    (101, "Ravi", 25, "Valid"),      # TC01
    (-1, "Ravi", 25, "Invalid"),     # TC02
    (102, "", 30, "Invalid"),        # TC03
    (103, "Kumar", -5, "Invalid"),   # TC04
    (104, "Suresh", 40, "Valid"),    # TC05
])
def test_validate_customer(customer_id, customer_name, age, expected):
    assert validate_customer(customer_id, customer_name, age) == expected
