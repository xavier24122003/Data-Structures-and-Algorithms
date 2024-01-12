# Tran Huynh Trung Hieu
# N21DCCN122
# D21CQCN02-N


def gcd(a,b):
  if b == 0:
    return a
  return gcd(b,a%b)

print(gcd(8,4))

#gcd(8,4)
# 4 != 0: gdc(4,0)
# 0 == 0: return 4
