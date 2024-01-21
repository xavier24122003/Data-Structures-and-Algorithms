def printUnorderedPairs4(arrayA, arrayB):
  for i in range(len(arrayA)):
    for j in range(len(arrayB)):
      if arrayA[i] < arrayB[j]:
        print(str(arrayA[i]) + "," + str(arrayB[j]))
print("\n\n\n- Q4: ")
printUnorderedPairs4([1,5,2,7,4],[2,5,3,1,7])
