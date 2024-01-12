def recursiveDoll(doll):
  if doll == 1:
    return "All dolls are opened"
  return recursiveDoll(doll-1)

print(recursiveDoll(3))

# recursiveDoll(3) 
# 3 != 1 :recursiveDoll(2)
# 2 != 1 : recursiveDoll(1)
# 1 == 1 : All dolls are opened
