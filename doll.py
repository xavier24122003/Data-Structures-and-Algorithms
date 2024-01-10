def recursiveDoll(doll):
  if doll == 1:
    return "All dolls are opened"
  return recursiveDoll(doll-1)

print(recursiveDoll(3))