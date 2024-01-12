# Tran Huynh Trung Hieu
# N21DCCN122
# D21CQCN02-N


def firstMethod():
  secondMethod()
  print("This is first method")
  
def secondMethod():
  thirdMethod()
  print("This is second Method")
  
def thirdMethod():
  fourMethod()
  print("This is third Method")
  
def fourMethod():
  print("This is four Method")
  
print(firstMethod())
