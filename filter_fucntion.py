ages = [5, 12, 17, 18, 24, 32]

def myFunc(x):
  return x >=18

adults = filter(myFunc, ages)

for x in adults:
  print(x)
