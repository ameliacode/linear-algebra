# Problem 2.5.1 eve is evil 10001


def binary2digit(seq: str) -> int:
    return int(seq, 2)


def cyper2plain(seq: str, key: str) -> str:
    return "".join("1" if s != k else "0" for s, k in zip(seq, key))


def decrypt(cypertext: str, key: str) -> str:
    answer = []
    symbols = cypertext.split()
    for symbol in symbols:
        plain = cyper2plain(symbol, key)
        digit = binary2digit(plain)
        if digit == 26:
            answer.append(" ")
        else:
            answer.append(chr(digit + 97))

    return "".join(answer)


cypertext = "10101 00100 10101 01011 11001 00011 01011 10101 00100 11001 11010"
keys = [f"{i:05b}" for i in range(32)]

for key in keys:
    print(decrypt(cypertext, key), key)
