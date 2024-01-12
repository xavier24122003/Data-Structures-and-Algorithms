def giaiThua(n):
  if n == 1:
    return 1
  return giaiThua(n-1) * n

print(giaiThua(5))

# 5 != 0: giaiThua(4) * 5
# 4 != 0: giaiThua(3) * 4 * 5
# 3 != 0: giaiThua(2) * 3 * 4 * 5
# 2!= 0: giaiThua(1) * 2 * 3 * 4 * 5
# 1 == 1: 1 * 2 * 3 * 4 * 5 = 120
