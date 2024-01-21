def printUnorderedPairs3(array):
  for i in range(0,len(array)):
    for j in range(i+1,len(array)):
      print(str(array[i]) + "," + str(array[j]))
print("\n\n\n- Q3: ")
printUnorderedPairs3([1,5,2,7,4])
