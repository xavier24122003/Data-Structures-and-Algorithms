# Tran Huynh Trung Hieu
# N21DCCN122
# D21CQCN02-N


def sumOfDigits(n):
  if n == 0:
    return 0
  return n%10 + sumOfDigits(n//10)

print(sumOfDigits(52))

# 52 != 0: 2 + sumOfDigits(5)
# 5 != 0: 2 + ( 5 + sumOfDigits(0))
# 0 = 0: 2 + ( 5 + 0) = 7
