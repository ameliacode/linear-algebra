import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ops import scalar_vector_mult

from utils.plotting import plot

# Task 3.5.4

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


plot(scalar_vector_mult(0.5, L), 4)
plot(scalar_vector_mult(-0.5, L), 4)
