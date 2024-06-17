"""
Given a natural number n, find the sum of all numbers upto n that are multiples of 3 and 5
"""
from typing import List, Optional

MULTIPLE_VALUES = [3,5]

def check_for_multiple(num_to_check: int, multi_values: Optional[List[int]] = MULTIPLE_VALUES) -> bool:
    """
    Method to check if num_to_check is a multiple
    of values in multi_values. Returns True if
    a multiple is found
    """

    multi_check = False
    for num in multi_values:
        if num_to_check % num == 0:
            multi_check = True

    return multi_check


num_to_test = 1000

ans = 0

for val in range(num_to_test):

    if check_for_multiple(val):
        ans += val

print(f'Result: {ans}')