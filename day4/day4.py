import sys

# TODO: make grid , word and directions global variables somehow, so won't have to pass
# TODO: split isWordConnected into isWordConnected and isCharacterConnected
# TODO: add comments and readme
# TODO: type hinting


class Puzzle:
    def __init__(self, filename: str, targetWord: str) -> None:
        self.filename: str = filename
        self.targetWord: str = targetWord
        self.grid: list[list[str]] = createGridFromFile(filename)

    def solve(self) -> int:
        firstLetter = self.targetWord[0]

        numMatches = 0
        directions = ["N","S","W","E","NW","NE","SW","SE"]

        # Go over every character in the grid
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                # If the first letter of the word is found, search for the rest of
                # the word in every possible direction and count the number of matches
                if self.grid[row][col] == firstLetter:
                    charsLeft = self.targetWord[1:]
                    for direction in directions:
                        if self.isWordConnected(row, col, charsLeft, self.targetWord, direction):
                            numMatches += 1
        return numMatches
    
    def isWordConnected(self, curRow, curCol, lettersLeft, word, direction) -> bool:
    # Base case for recursion (empty string means whole word found)
        if not lettersLeft:
            return True
        
        targetLetter = lettersLeft[0]
        if self.isTargetLetterConnected(curRow, curCol, targetLetter, direction):
            return self.isWordConnected(
                    nextRow, nextCol, lettersLeft[1:], word, directio
                

        return False

    def isTargetLetterConnected(self, curRow, curCol, targetLetter, direction):
        nextRow, nextCol = self.getNextCoordinateInDirection(curRow, curCol, direction)

        if self.isValidCoordinate(nextRow, nextCol, self.grid):
            nextLetter = self.grid[nextRow][nextCol]
            if nextLetter == targetLetter:
                return True
        return False

    def getNextCoordinateInDirection(row, col, direction):
        directions = {
            "N": {"row": row - 1, "col": col},
            "S": {"row": row + 1, "col": col},
            "W": {"row": row, "col": col - 1},
            "E": {"row": row, "col": col + 1},
            "NW": {"row": row - 1, "col": col - 1},
            "NE": {"row": row - 1, "col": col + 1},
            "SW": {"row": row + 1, "col": col - 1},
            "SE": {"row": row + 1, "col": col + 1},
        }

        nextRow = directions[direction][row]
        nextCol = directions[direction][col]

        return nextRow, nextCol

    def isValidCoordinate(row, col, grid) -> bool:
        minIdx = 0
        maxRowIdx = len(grid) - 1
        maxColIdx = len(grid[0]) - 1
        return (minIdx <= row <= maxRowIdx) and (minIdx <= col <= maxColIdx)


def main() -> None:

    try:
        filename: str = sys.argv[1]
    except IndexError:
        exit("Usage: python day4.py filename")

    targetWord = input("Enter target word: ").upper()
    puzzle = Puzzle(filename, targetWord)
    solution = puzzle.solve()
    print(f"The word {targetWord} occurs {solution} times in {filename}.")


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
