import math

from plotting import plot


# Problem 2.7.1
def my_filter(L: list, num: int) -> list:
    return [i for i in L if i % num != 0]


print(my_filter([1, 2, 4, 5, 7], 2))


# Problem 2.7.2
def my_list(L: list) -> list:
    return [[i for i in range(1, x + 1)] for x in L]


print(my_list([1, 2, 3]))
print(my_list([0]))


# Problem 2.7.3
def my_function_composition(f: dict, g: dict) -> dict:
    result = {}
    for f_key in f.keys():
        result[f_key] = g[f[f_key]]
    return result


print(my_function_composition({0: "a", 1: "b"}, {"a": "apple", "b": "banana"}))


# Problem 2.7.4
def mySum(L: list) -> float:
    current = 0
    for x in L:
        current += x
    return current


# Problem 2.7.5
def myProduct(L: list) -> float:
    current = 1
    for x in L:
        current *= x
    return current


# Problem 2.7.6
def myMin(L: list) -> float:
    current = float("inf")
    for x in L:
        if current < x:
            current = x
    return current


# Problem 2.7.7
def myConcat(L: list) -> list:
    current = ""
    for x in L:
        current = current + x
    return current


# Problem 2.7.8
def myUnion(L: list) -> list:
    current = set()
    for x in L:
        current = current | x
    return current


# Problem 2.7.9
bin = my_list([])
print(mySum(bin))
print(myProduct(bin))
print(myMin(bin))
print(myConcat(bin))
print(myUnion(bin))


# Problem 2.7.12
def transform(a: complex, b: complex, L: list) -> list:
    result = []
    for z in L:
        result.append(a * z + b)

    return result


S = [
    2 + 2j,
    3 + 2j,
    1.75 + 1j,
    2 + 1j,
    2.25 + 1j,
    2.5 + 1j,
    2.75 + 1j,
    3 + 1j,
    3.25 + 1j,
]
answer_a = transform(2j, 1 + 1j, S)
plot(answer_a, 8)

answer_b = transform((2 + 3j) * (math.e ** (math.pi * 1j / 4)), -3 - 2j, S)
plot(answer_b, 8)
