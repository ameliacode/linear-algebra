import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ops import add2, scalar_vector_mult

from utils.plotting import plot

plot([add2(scalar_vector_mult(i / 100.0, [3, 2]), [0.5, 1]) for i in range(101)], 4)

# Task 3.6.9


def segment(pt1: list, pt2: list) -> list:
    v = [pt2[0] - pt1[0], pt2[1] - pt1[1]]
    return [add2(scalar_vector_mult(i / 100, v), pt1) for i in range(101)]


plot(segment(pt1=[3.5, 3], pt2=[0.5, 1]))
