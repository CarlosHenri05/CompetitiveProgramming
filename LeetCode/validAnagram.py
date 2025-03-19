from collections import Counter

def validAnagram(s,t):
  if len(s)!=len(s):
    return False  
  
  countS = Counter(s)
  countT = Counter(t)

  if (countS==0 and countT == 0):
    return True
  return False
