def recursiveMethod(n):
  if n == 0:
    return "Less than 1"
  recursiveMethod(n-1)
  print(n)

print(recursiveMethod(20))