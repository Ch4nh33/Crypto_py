import re 

flag = "63727970746f7b5976f755f77696c6c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"

PLAINTEXT = ""

result = re.findall('..?', flag)
print(result)

for i in result:
  i = int( i , 16 )
  PLAINTEXT = PLAINTEXT + chr(i)
  
print(PLAINTEXT)
