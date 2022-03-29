import math

def NthFibonacci(n):
  fiveSquare = math.sqrt(5)
  return round((1/fiveSquare)*(((1 + fiveSquare)/2)**n - ((1 - fiveSquare)/2)**n)) 

fibonacciNumber = 1
while fibonacciNumber:
  try:
    NthFibonacci(fibonacciNumber)
  except:
    print('out of range')
    break
  else:
    print(NthFibonacci(fibonacciNumber))
    
  fibonacciNumber += 1

print(fibonacciNumber)


# fibonacciResults = []
# for i in range(maxFibonacci + 1):
#   fibonacciResults.append(NthFibonacci(i))
# print(fibonacciResults)

