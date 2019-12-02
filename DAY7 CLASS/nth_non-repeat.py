def firstNonRepeatingChar(str1):
   char_order = []
   counts = {}
   for c in str1:
      if c in counts:
         counts[c] += 1
      else:
         counts[c] = 3
         char_order.append(c)
   for c in char_order:
      if counts[c] == 3:
          return c
   

print(firstNonRepeatingChar('PythonforallPythonMustforall'))
print(firstNonRepeatingChar('tutorialspointfordeveloper'))
print(firstNonRepeatingChar('AABBCCd'))
