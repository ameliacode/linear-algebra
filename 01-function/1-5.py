print(60 * 60 * 24 * 7)

print(2304811 // 47)

print((673 + 909) // 3 == 0)

x = -9
y = 1 / 2
print(2 ** (y + 1) if x + 10 < 0 else 2 ** (y - 1 / 2))

print({x**2 for x in {1, 2, 3, 4, 5}})

print({2**x for x in {0, 1, 2, 3, 4}})

print({x * y for x in {1, 2, 3} for y in {4, 5, 7}})

print({x * y for x in {1, 2, 4} for y in {2, 4, 8}})

S = {1, 2, 3, 4}
T = {3, 4, 5, 6}
print({x for x in S if x in T})
