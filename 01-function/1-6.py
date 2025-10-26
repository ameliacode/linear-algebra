import cmath
import math

# Task 1.6.1
print(cmath.sqrt(-1), math.cos(math.pi), math.log(math.e))


# Task 1.6.2
from random import randint


def movie_review(name: str) -> str:
    movie_reviews = ["See it!", "A gem!", "Ideological claptrapl!"]
    return f"{movie_reviews[randint(0, len(movie_reviews) - 1)]} {name} {movie_reviews[randint(0, len(movie_reviews) - 1)]}"


print(movie_review("Interstellar"))

# Task 1.6.3
# from imp import reload -> DeprecationWarning: removal in Python 3.12

# Task 1.6.4
from dictutil import listrange2dict

print(listrange2dict(["A", "B", "C"]))
