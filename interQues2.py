# Tran Huynh Trung Hieu
# N21DCCN122
# D21CQCN02-N


def powerOfNumber(x,n):
  if n == 0:
    return 1
  return x * powerOfNumber(x,n-1)

print(powerOfNumber(3,4))

# 4 != 0: 3 * powerOfNumber(3,3)
# 3 != 0: 3 * 3 * powerOfNumber(3,2)
# 2 != 0: 3 * 3 * 3 * powerOfNumber(3,1)
# 1 != 0: 3 * 3 * 3 * 3 powerOfNumber(3,0)
# 0 == 0: 3 * 3 * 3 * 3 * 1 =81

