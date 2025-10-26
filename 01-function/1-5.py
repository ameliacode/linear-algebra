# Task 1.5.1
print(60 * 60 * 24 * 7)

# Task 1.5.2
print(2304811 // 47)

# Task 1.5.3
print((673 + 909) // 3 == 0)

# Task 1.5.4
x = -9
y = 1 / 2
print(2 ** (y + 1) if x + 10 < 0 else 2 ** (y - 1 / 2))

# Task 1.5.5
print({x**2 for x in {1, 2, 3, 4, 5}})

# Task 1.5.6
print({2**x for x in {0, 1, 2, 3, 4}})

# Task 1.5.7
print({x * y for x in {1, 2, 3} for y in {4, 5, 7}})

# Task 1.5.8
print({x * y for x in {1, 2, 4} for y in {2, 4, 8}})

# Task 1.5.9
S = {1, 2, 3, 4}
T = {3, 4, 5, 6}
print({x for x in S if x in T})

# Task 1.5.10
value = [20, 10, 15, 75]
print(sum(value) / len(value))

# Task 1.5.11
print([[x, y] for x in ["A", "B", "C"] for y in [1, 2, 3]])

# Task 1.5.12
LoFL = [[0.25, 0.75, 0.1], [-1, 0], [4, 4, 4, 4]]
print(sum([sum(x) for x in LoFL]))

# Task 1.5.13
# print([x,y] = [4*1,4*2,4*3,4*4]) # SyntaxError

# Task 1.5.14
S = {-4, -2, 1, 2, 5, 0}
print([(i, j, k) for i in S for j in S for k in S if i + j + k == 0])

# Task 1.5.15
print(
    [
        (i, j, k)
        for i in S
        for j in S
        for k in S
        if i + j + k == 0 and not (i is 0 and j is 0 and k is 0)
    ]
)

# Task 1.5.16
print(
    [
        (i, j, k)
        for i in S
        for j in S
        for k in S
        if i + j + k == 0 and i != j and j != k
    ][0]
)

# Task 1.5.17
L = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
print(len(L) == len(list(set(L))))

# Task 1.5.18
print(set(x for x in range(1, 100) if x % 2 != 0))

# Task 1.5.19
L = ["A", "B", "C", "D", "E"]
print(list(zip(range(len(L)), L)))

# Task 1.5.20
x = [10, 25, 40]
y = [1, 15, 20]
print(list(sum(i) for i in zip(x, y)))

# Task 1.5.21
dlist = [
    {"James": "Sean", "director": "Terence"},
    {"James": "Roger", "director": "Lewis"},
    {"James": "Pierce", "director": "Roger"},
]
k = "James"
print([i[k] for i in dlist])

# Task 1.5.22
dlist = [{"Bilbo": "Ian", "Frodo": "Elijah"}, {"Bilbo": "Martin", "Thorin": "Richard"}]
k = "Bilbo"
print(i[k] if k in i else "NOT PRESENT" for i in dlist)
k = "Frodo"
print(i.get(k, "NOT PRESENT") for i in dlist)

# Task 1.5.23
print({x: x * x for x in range(100)})

# Task 1.5.24
D = {"red" "white", "blue"}
print({x: x for x in D})

# Task 1.5.25
base = 10
digits = set(range(base))
print(
    {
        x: [x // base // base // base, x // base % base, x % base]
        for x in range(base * base * base)
    }
)

# Task 1.5.26
id2salary = {0: 1000.0, 3: 990, 1: 1200.50}
names = ["Larry", "Curly", "", "Moe"]
print({names[k]: id2salary.get(k) for k in id2salary.keys()})


# Task 1.5.27
def twice(z):
    return 2 * z


print(twice(int(input())))


# Task 1.5.28
def nextInts(L: list) -> list:
    return [i + 1 for i in L]


print(nextInts([1, 5, 7]))


# Task 1.5.29
def cubes(L: list) -> list:
    return [i**3 for i in L]


print(cubes([1, 2, 3]))


# Task 1.5.30
def dict2list(dct: dict, keylist: list) -> list:
    return [dct[k] for k in keylist]


print(dict2list({"a": "A", "b": "B", "c": "C"}, ["b", "c", "a"]))


# Task 1.5.31
def list2dict(L: list, keylist: list) -> dict:
    return {L[i]: keylist[i] for i in range(len(L))}


print(list2dict(["A", "B", "C"], ["a", "b", "c"]))


# Task 1.5.32
def all_3_digit_numbers(base: int, digits: set) -> set:
    return set(
        sum((i * base**2, j * base, k)) for i in digits for j in digits for k in digits
    )


base = 2
print(all_3_digit_numbers(base, set(range(base))))
