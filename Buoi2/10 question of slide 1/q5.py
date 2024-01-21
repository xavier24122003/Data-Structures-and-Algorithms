def printUnorderedPairs5(arrayA, arrayB):
  for i in range(len(arrayA)):
    for j in range(len(arrayB)):
      for k in range(0,100000):
        print(str(arrayA[i]) + "," + str(arrayB[j]))
print("\n\n\n- Q5: ")
printUnorderedPairs5([1,5,2,7,4],[2,5,3,1,7])
