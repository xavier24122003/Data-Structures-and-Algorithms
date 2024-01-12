def powerOfTwo(n):
  if n == 0:
    return 1
  return powerOfTwo(n-1) * 2

print(powerOfTwo(5))

# 5 != 0: 2 * powerOfTwo(4)
# 4 != 0: 2 * 2 * powerOfTwo(3)
# 3 != 0: 2 * 2 * 2 * powerOfTwo(2)
# 2 != 0: 2 * 2 * 2 * 2 * powerOfTwo(1)
# 1 != 0: 2 * 2 * 2 * 2 * 2 * powerOfTwo(0)
# 0 == 0: 2 * 2 * 2 * 2 * 2 * 1 = 32
