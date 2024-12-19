import sys
import re


def main() -> None:

    try:
        filename: str = sys.argv[1]
    except IndexError:
        exit("Usage: python day3.py filename")

    data: str = getDataFromFile(filename)
    validMuls: list = getValidMuls(data)

    print(f"Solution part 1: {addMuls(validMuls)}")

    data = removeDisabledMuls(data)
    validMuls = getValidMuls(data)
    print(f"Solution part 2: {addMuls(validMuls)}")


def addMuls(muls) -> int:
    total: int = 0
    for mul in muls:
        n1: str = re.findall("[0-9][0-9]?[0-9]?", mul)[0]
        n2: str = re.findall("[0-9][0-9]?[0-9]?", mul)[1]
        total += int(n1) * int(n2)
    return total


def getValidMuls(data) -> list:
    return re.findall(r"mul\([0-9][0-9]?[0-9]?,[0-9][0-9]?[0-9]?\)", data)

def removeDisabledMuls(data) -> str:
    # To remove all muls preceded by a don't, keep doing this:
    # search for a string starting with 'don't()' and ending with 'do()'.
    # all muls between this will be invalid.
    # remove this entire part from the data using the start and end index.
    while True:
        match = re.search(r"don't\(\).*?do\(\)", data)
        if not match: break
        
        data = data[:match.start()] + data[match.end():]

    return data



def getDataFromFile(filename) -> str:
    with open(filename) as file:
        string: str = ""
        for line in file:
            string += line.replace("\n", "").strip()
    return string


if __name__ == "__main__":
    main()
