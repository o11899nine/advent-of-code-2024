from day2 import allIncreasing, allDecreasing, correctDifferences

def testAllIncreasing():
  assert allIncreasing([1,2,3,4,5]) == True
  assert allIncreasing([2,4,6,7,8]) == True
  assert allIncreasing([2,4,6,6,8]) == False
  assert allIncreasing([7,4,6,6,8]) == False
  assert allIncreasing([1,2,3,4,4]) == False
  assert allIncreasing([1,2,3,4,3]) == False
  assert allIncreasing([5,4,3,2,1]) == False
  assert allIncreasing([5,4,3,2,3]) == False

def testAllDecreasing():
  assert allDecreasing([5,4,3,2,1]) == True
  assert allDecreasing([8,7,5,4,2]) == True
  assert allDecreasing([8,5,5,4,2]) == False
  assert allDecreasing([8,9,5,4,2]) == False
  assert allDecreasing([8,7,5,4,4]) == False
  assert allDecreasing([8,7,5,4,6]) == False

def testCorrectDifferences():
  assert correctDifferences([1,2,3,4,5]) == True
  assert correctDifferences([5,4,3,2,1]) == True
  assert correctDifferences([1,3,5,7,9]) == True
  assert correctDifferences([9,7,5,3,1]) == True
  assert correctDifferences([1,4,7,10,13]) == True
  assert correctDifferences([13,10,7,4,1]) == True
  assert correctDifferences([13,9,7,4,1]) == False
  assert correctDifferences([9,7,6,5,5,3]) == False
  assert correctDifferences([1,2,7,9,10]) == False