def reverseInt(num):
  strNum = str(num)
  strNum = strNum[::-1]
  return int(strNum)
  
n = int(input("Nhap vao mot so nguyen: "))
print(type(reverseInt(n)))
print(reverseInt(n))
