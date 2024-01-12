def recursiveMethod(n):
  if n == 0:
    return "Less than 1"
  recursiveMethod(n-1)
  print(n)

print(recursiveMethod(3))

# 3 != 0: recursiveMethod(2)
# 2 != 0: recursiveMethod(1)
# 1 != 0: recursiveMethod(0)
# 0 = 0: Less than 1
