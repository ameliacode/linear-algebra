# Problem 2.5.1
from GF2 import one


def binary2digit(seq: str, key: str) -> int:
    


def decode(code: str) -> str:
    answer = []
    symbols = code.split()
    for symbol in symbols:
        digit = binary2digit(symbol)
        if digit == 26:
            answer.append(" ")
        else:
            answer.append(chr(digit + 97))

    return "".join(answer)


code = "10101 00100 10101 01011 11001 00011 01011 10101 00100 11001 11010"
print(decode(code))
