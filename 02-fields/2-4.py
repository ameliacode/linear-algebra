from image import file2image
from plotting import plot

# Task 2.4.1
S = {
    2 + 2j,
    3 + 2j,
    1.75 + 1j,
    2 + 1j,
    2.25 + 1j,
    2.5 + 1j,
    2.75 + 1j,
    3 + 1j,
    3.25 + 1j,
}
plot(S, 4)

# Task 2.4.3
plot({1 + 2j + z for z in S}, 4)

# Task 2.4.7 "My scaled points"
plot({0.5 * z for z in S}, 4)

# Task 2.4.8 "Rotated and scaled"
plot({z * -1j * 0.5 for z in S}, 4)

# Task 2.4.9
plot({z * -1j * 0.5 + (2 - 1j) for z in S}, 4)

# Task 2.4.10
data = file2image("img01.png")
height, width = len(data), len(data[0])

pts = []
for y in range(height):
    for x in range(width):
        if data[y][x][0] < 120:
            pts.append(x - y * 1j + height * 1j)

plot(pts, 190)


# Task 2.4.11
def f(z: complex) -> list:
    pts = []
    for s in S:
        pts.append(s + z)
    return pts


z = 1 + 2j
plot(f(z), 4)


# Task 2.4.12
def scale(factor: float) -> list:
    pts = []
    for s in S:
        pts.append(s * -1j * factor)
    return pts


plot(scale(0.5), 4)

# Task 2.4.17
import math


def w(t: int) -> complex:
    return math.e ** (t * 2 * math.pi * 1j / 20)


plot({w(i) for i in range(20)}, 4)


# Task 2.4.18
plot({math.e ** (math.pi * 1j / 4) * s for s in S}, 4)

# Task 2.4.19
plot({math.e ** (math.pi * 1j / 4) * pt for pt in pts}, 190)

# TAsk 2.4.20
plot(
    {
        math.e ** (math.pi * 1j / 4) * (pt - width / 2 - height / 2 * 1j) * 0.5
        for pt in pts
    },
    190,
)
