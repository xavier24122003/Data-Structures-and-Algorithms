#q1: Tinh tong va tich cua mot chuoi
def foo(array):
  sum = 0
  product = 1
  for i in array:
    sum += i
  for i in array:
    product *= i
  return "Sum = "+str(sum)+", Product = "+str(product)
  
print(f"- Q1: {foo([2,5,3,1,7])}")
