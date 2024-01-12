# Tran Huynh Trung Hieu
# N21DCCN122
# D21CQCN02-N

def covertDeToBi(n):
  assert n >= 0 and int(n) == n
  if n == 0:
    return 0
  return n%2 + 10*covertDeToBi(n//2)

print (covertDeToBi(5))

# = 1 + 10 * convertDeToBi(2)
# = 1 + 10 * (0 + 10 * convertDeToBi(1))
# = 1 + 10 * (10 * (1 + 10 * convertDeToBi(0))
# = 1 + 10 * (10 * (1 + 10 * 0))= 101
