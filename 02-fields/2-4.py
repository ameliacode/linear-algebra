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
file2image("img01.png")
