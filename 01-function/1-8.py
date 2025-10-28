# Problem 1.8.1
def increments(L: list) -> list:
    return [i + 1 for i in L]


print(increments([1, 5, 7]))


# Problem 1.8.2
def cubes(L: list) -> list:
    return [i**3 for i in L]


print(cubes([1, 2, 3]))


# Problem 1.8.3
def triple_sum(A: list, B: list) -> list:
    result = []
    for (x, y), (z, w) in zip(A, B):
        result.append((x + z, y + w))
    return result


print(triple_sum([(1, 2), (10, 20)], [(3, 4), (30, 40)]))


# Problem 1.8.4
def inv_dict(d: dict) -> dict:
    return {d[k]: k for k in d.keys()}


print(inv_dict({"thank you": "merci", "goodbye": "au revoir"}))


# Problem 1.8.5
def row(p: int, v: int) -> list:
    return [p + i for i in range(v)]


print(row(10, 4))
print([row(i, 20) for i in range(15)])
print([[i + j for j in range(20)] for i in range(15)])
