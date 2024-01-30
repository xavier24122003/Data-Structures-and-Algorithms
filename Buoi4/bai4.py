def isAnagrams(str1,str2):
  if len(str2) != len(str1):
    return False
  for i in str1:
    if i not in str2:
      return False
  return True

str1 = "restful"
str2 = "fluster"
print(isAnagrams(str1,str2))






  