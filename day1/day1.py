import sys

def main():

  # Get filename from command line
  filename: str = sys.argv[1]

  # Create two lists (left and right) from data
  leftList: list[int] = []
  rightList: list[int] = []
  leftList, rightList = splitData(filename)

  # Sort the lists ascending
  leftList.sort()
  rightList.sort()

  # Calculate total difference
  totalDifference = 0
  for i in range(len(leftList)):
      totalDifference += abs(leftList[i] - rightList[i])

  print(f"Total difference: {totalDifference}")

  # Calculate similarity score
  similarityScore = 0

  for id in leftList:
      # Count how often left id appears in right list
      appearances = rightList.count(id)
      similarityScore += id * appearances
  
  print(f"Similarity score: {similarityScore}")
  
  
def splitData(filename: str) -> tuple[list, list]:
    leftList: list[int] = []
    rightList: list[int] = []

    with open(filename) as file:
        for line in file:
            line: str = line.replace("\n", "")
            splitLine = line.split()
            leftList.append(int(splitLine[0]))
            rightList.append(int(splitLine[1]))

    return leftList, rightList

if __name__ == "__main__":
    main()