import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ops import add2

from utils.plotting import plot

# Task 3.4.3

L = [
    [2, 2],
    [3, 2],
    [1.75, 1],
    [2, 1],
    [2.25, 1],
    [2.5, 1],
    [2.75, 1],
    [3, 1],
    [3.25, 1],
]


plot([add2(v, [1, 2]) for v in L], 4)
