import cmath
import math
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

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
from utils.dictutil import listrange2dict

print(listrange2dict(["A", "B", "C"]))

f = open("stories_big.txt")
stories_big = list(f)
f = open("stories_small.txt")
stories_small = list(f)


# Task 1.6.6
def makeInverseIndex(strlist: list) -> dict:
    indexes = {}
    keys = set()
    for strings in strlist:
        words = set(strings.split())
        keys |= words
    for key in keys:
        indexes[key] = set()
    for key in keys:
        for i, strings in enumerate(strlist):
            if key in strings:
                indexes[key].add(i)
    return indexes


inverseIndex = makeInverseIndex(stories_small)
query = ["secret", "the"]


# Task 1.6.7
def orSearch(inverseIndex: dict, query: list) -> set:
    values = list()
    for q in query:
        values.append(inverseIndex[q])
    return set.union(*values)


print(orSearch(inverseIndex, query))


# Task 1.6.8
def andSearch(inverseIndex: dict, query: list) -> set:
    values = list()
    for q in query:
        values.append(inverseIndex[q])
    return set.intersection(*values)


print(andSearch(inverseIndex, query))
