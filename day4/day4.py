import sys

# TODO: make grid , word and directions global variables somehow, so won't have to pass
# TODO: split isWordConnected into isWordConnected and isCharacterConnected
# TODO: add comments and readme
# TODO: type hinting
# TODO: publish to github as separate project


def main() -> None:

    try:
        filename: str = sys.argv[1]
    except IndexError:
        exit("Usage: python day4.py filename")

    grid: list[list] = createGridFromFile(filename)

    word = input("Enter target word: ").upper()
    firstLetter = word[0]

    numMatches = 0
    directions = [
        "up",
        "down",
        "left",
        "right",
        "topLeft",
        "topRight",
        "bottomLeft",
        "bottomRight",
    ]

    # Go over every character in the grid
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            # If the first letter of the word is found, search for the rest of
            # the word in every possible direction and count the number of matches
            if grid[row][col] == firstLetter:
                for direction in directions:
                    if isWordConnected(row, col, grid, word[1:], word, direction):
                        numMatches += 1

    print(f"{word} occurs {numMatches} times in {filename}!")


def isWordConnected(row, col, grid, string, word, direction) -> bool:
    # Base case for recursion (empty string means whole word found)
    if not string:
        return True

    directions = {
        "up": {"row": row - 1, "col": col},
        "down": {"row": row + 1, "col": col},
        "left": {"row": row, "col": col - 1},
        "right": {"row": row, "col": col + 1},
        "topLeft": {"row": row - 1, "col": col - 1},
        "topRight": {"row": row - 1, "col": col + 1},
        "bottomLeft": {"row": row + 1, "col": col - 1},
        "bottomRight": {"row": row + 1, "col": col + 1},
    }

    targetRow = directions[direction]["row"]
    targetCol = directions[direction]["col"]

    targetChar = string[0]

    if isValidCoordinate(targetRow, targetCol, grid):
        char = grid[targetRow][targetCol]

        # If target character has been found, search the next one
        if char == targetChar:
            return isWordConnected(
                targetRow, targetCol, grid, string[1:], word, direction
            )

    return False


def isValidCoordinate(row, col, grid) -> bool:
    minIdx = 0
    maxRowIdx = len(grid) - 1
    maxColIdx = len(grid[0]) - 1
    return (minIdx <= row <= maxRowIdx) and (minIdx <= col <= maxColIdx)


def createGridFromFile(filename) -> list[list]:
    grid: list[list] = []

    with open(filename) as file:
        for line in file:
            line = line.strip()
            line = line.upper()
            row = list(line)
            grid.append(row)

    return grid


if __name__ == "__main__":
    main()
