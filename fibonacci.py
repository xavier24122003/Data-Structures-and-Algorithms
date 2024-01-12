# Tran Huynh Trung Hieu
# N21DCCN122
# D21CQCN02-N

def fibonacci(n):
  if n in [1,2]:
    return 1
  return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(3))

# 3 not in [1,2] : fibonacci(2) + fibonacci(1)
# 2, 1 in [1,2]: 1 + 1 = 2
