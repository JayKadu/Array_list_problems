
def missingNumber(myList,totalCount):
  expectedSum=totalCount*((totalCount+1)/2)
  actualSum=0
  for i in myList:
    actualSum+=i
  return int(expectedSum-actualSum)
print(missingNumber([1,2,3,4,6],6))
