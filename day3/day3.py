import sys
import re


def main() -> None:
    try:
        filename: str = sys.argv[1]
    except IndexError:
        exit("Usage: python day3.py filename")

    dataString: str = createDataString(filename)
    validMuls: list = getValidMuls(dataString)

    print(addMuls(validMuls))


def addMuls(muls) -> int:
    total: int = 0
    for mul in muls:
        n1: str = re.findall("[0-9][0-9]?[0-9]?", mul)[0]
        n2: str = re.findall("[0-9][0-9]?[0-9]?", mul)[1]
        total += int(n1) * int(n2)
    return total


def getValidMuls(str) -> list:
    return re.findall(r"mul\([0-9][0-9]?[0-9]?,[0-9][0-9]?[0-9]?\)", str)


def createDataString(filename) -> str:
    with open(filename) as file:
        string: str = ""
        for line in file:
            string += line.replace("\n", "").strip()
    return string


if __name__ == "__main__":
    main()
