import math
import random
import time
firstLenghtTime = 0
secondLenghtTime = 0

def NthFibonacci(n):
  fiveSquare = math.sqrt(5)
  return round((1/fiveSquare)*(((1 + fiveSquare)/2)**n - ((1 - fiveSquare)/2)**n)) 

def FromFormula(num):
  start_time = time.time()
  # for i in range(loopsNumber):
    # num = random.randrange(maxFibonacciNumber + 1)
  print(NthFibonacci(num))
  firstLenghtTime = time.time() - start_time
  print("---it took %f seconds to execute the formula---" % (firstLenghtTime))
  return NthFibonacci(num)
  
# the first 40 Fibonacci numbers
fibonacciResults = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986, 102334155]
  
def FromCache(num):
  start_time = time.time()
  # global result
  print(fibonacciResults[num])
  secondLenghtTime = time.time() - start_time
  # result = [fibonacciResults[num], secondLenghtTime]
  print("---it took %f seconds to execute with the cache---" % (secondLenghtTime)) 
  return fibonacciResults[num]
