x = input("Input a number:")

rnew = int(x)

for i in range(4):
  r1 = rnew
  r2 = int(x)/r1
  rnew = (r1 + r2)/2
  print(r1, rnew, r2)