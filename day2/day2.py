import sys


def main() -> None:

    # Get filename from command line
    filename: str = sys.argv[1]

    reports: list[list[int]] = separateReports(filename)

    numSafeReports: int = 0

    for report in reports:
        if (allIncreasing(report) or allDecreasing(report)) and correctDifferences(report):
            numSafeReports += 1
        
    print(f"Number of safe reports: {numSafeReports}")

def correctDifferences(report: list[int]) -> bool:
    # For each level, check if difference to next level is between 1 and 3
    # Don't check the last level: len(report) - 1
    for i in range(len(report) - 1):
        difference: int = abs(report[i] - report[i + 1])
        if not 1 <= difference <= 3:
            return False
    return True

def allDecreasing(report: list[int]) -> bool:
    # For each level, check if next level is smaller
    # Don't check the last level: len(report) - 1
    for i in range(len(report) - 1):
        if not report[i] > report[i + 1]:
            return False
    return True


def allIncreasing(report: list[int]) -> bool:
    # For each level, check if next level is bigger
    # Don't check the last level: len(report) - 1
    for i in range(len(report) - 1):
        if not report[i] < report[i + 1]:
            return False
    return True


def separateReports(filename: str) -> list[list[int]]:
    reports: list[list[int]] = []

    with open(filename) as file:
        for line in file:
            report: list = line.split()

            # Convert every item to int
            for i in range(len(report)):
                report[i] = int(report[i])

            reports.append(report)
            
    return reports


if __name__ == "__main__":
    main()
