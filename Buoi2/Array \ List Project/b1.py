#Tran Huynh Trung Hieu
#N21DCCN122
#D21CQCN02-N


from array import *

#Tinh trung binh
def average(a):
  sum = 0
  for i in a:
    sum += i
  average = sum / len(a)
  return average

#Dem so ngay tren nhiet do trung binh
def aboveAverage(arr, average):
  count = 0
  for i in range(len(arr)):
    if arr[i] > average:
      count += 1
  return count

n = int(input('How many day\'temperature? ' ))
arr = array('i',[int(input(f'Day {i}\'s high temp : ')) for i in range(1,n+1)])
print(f"Average: {average(arr)}")
print(f"{aboveAverage(arr,average(arr))} day(s) above average")


  
