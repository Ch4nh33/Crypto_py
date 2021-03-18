def gcd(a,b):
  
  if a<b:
    a,b = b,a
  
  while b != 0:
    a,b = ba%b
   
  return a
print(gcd(66528,52920))
