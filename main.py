x= "StopAndSmellTheFlowers"
size = len(x)
for i in range(size):
  if i==0:
    x+=x[i]
  elif x[i] == x[i].upper():
    x+=" "+x[i]
  else:
    x+=x[i]
print(x[size:])
