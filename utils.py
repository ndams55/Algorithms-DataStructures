"""Defining global utils functions for the packages"""

from search_Problem.static_array import *
from collections import defaultdict


def birthday_match(students: dict) -> None:
    
    n = len(students)
    record = StaticArray(n)

    for k in range(n):
        (name1, bday1) = students[k]
        for i in range(k):
            (name2, bday2) = record.__getattr__(i)
            if bday1 == bday2:
                return (name1, name2)
        record.__setattr__(k, (name1, bday1))

    return None