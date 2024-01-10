def powerOfNumber(x,n):
  if n == 0:
    return 1
  return x * powerOfNumber(x,n-1)

print(powerOfNumber(2,6))
