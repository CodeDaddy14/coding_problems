# Implement a function that compresses a string using the counts of repeated characters.
  
# Example: "aabcccccaaax" → "a2b1c5a3"

from collections import Counter

from itertools import groupby

def compress_counter(a):
    return "".join(f"{ch}{len(list(group))}" for ch, group in groupby(a))

def compress(a):
  i = 0
  result = ""
  count = 0
  print(len(a))
  while i<len(a)-1:
    print([i,a[i]])
    count += 1
    if a[i]!=a[i+1]:
      result = result + a[i] + str(count)
      count = 0  
    i+=1
  result = result + a[-1] + str(count+1)


  return result
      
      

print(compress("aabcccccaaab"))
