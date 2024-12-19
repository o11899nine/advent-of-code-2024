import sys

# TODO: make grid and directions global variables somehow, so won't have to pass
# TODO: better function name for countMatches
# TODO: split functions?
# TODO: add comments and readme
# TODO: publish to github as separate project

def main() -> None:

    try:
        filename: str = sys.argv[1]
    except IndexError:
        exit("Usage: python day4.py filename")

    grid = createGridFromFile(filename)

    word = input("Enter target word: ")
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
                    numMatches += countMatches(row, col, grid, word[1:], word, direction)
                

    print(f"{word} occurs {numMatches} times")


def countMatches(row, col, grid, string, word, direction):
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

    # Complete string has been found
    if not string:
        return 1
    
    targetChar = string[0]

    if isValidCoordinate(targetRow, targetCol, grid):
        char = grid[targetRow][targetCol]

        # If target character has been found, search the next one
        if char == targetChar:
            return countMatches(
                targetRow, targetCol, grid, string[1:], word, direction
            )
   
    return 0





def isValidCoordinate(rowIndex, colIndex, grid):
    maxRowIndex = len(grid) - 1
    maxColIndex = len(grid[0]) - 1
    return 0 <= rowIndex <= maxRowIndex and 0 <= colIndex <= maxColIndex


def createGridFromFile(filename) -> list[list]:
    grid: list[list] = []

    with open(filename) as file:
        for line in file:
            line = line.replace("\n", "")
            row: list[str] = []
            for char in line:
                row.append(char)

            grid.append(row)

    return grid


if __name__ == "__main__":
    main()
