import math

def NthFibonacci(n):
  fiveSquare = math.sqrt(5)
  return round((1/fiveSquare)*(((1 + fiveSquare)/2)**n - ((1 - fiveSquare)/2)**n)) 


loops = 101
maxFibonacci = 1475

for i in range(maxFibonacci + 1):
  NthFibonacci(i)





# fibonacciResults = []
# for i in range(maxFibonacci + 1):
#   fibonacciResults.append(NthFibonacci(i))
  
# print(fibonacciResults)

for i in range(maxFibonacci + 1):
  NthFibonacci(i)