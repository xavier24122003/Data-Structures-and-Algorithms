def covertDeToBi(n):
  assert n >= 0 and int(n) == n
  if n == 0:
    return 0
  return n%2 + 10*covertDeToBi(n//2)

print (covertDeToBi(9))