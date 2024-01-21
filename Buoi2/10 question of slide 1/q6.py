def reverse(array):
  for i in range(0, int(len(array)/2)):
    other = len(array)-i-1
    temp = array[i]
    array[i] = array[other]
    array[other] = temp
  print(array)
  
print("\n\n\n- Q6: ")
reverse([11,50,23,7,4])

#result: [4,7,11,23,50]
