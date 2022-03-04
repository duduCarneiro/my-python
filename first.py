import math
import random
import time

def NthFibonacci(n):
  fiveSquare = math.sqrt(5)
  return (1/fiveSquare)*(((1 + fiveSquare)/2)**n - ((1 - fiveSquare)/2)**n)

# applying formula - n from 0 to 40 - 1000 times
start_time = time.time()
for i in range(1001):
  num = random.randrange(41)
  print('using formula, what is the Fibonacci number of %d?'% num)
  print (round(NthFibonacci(num)))
firstLenghtTime = time.time() - start_time 
  
  

fibonacciResults = []
for i in range(41):
  fibonacciResults.append(round(NthFibonacci(i)))
  
# caching results - n from 0 to 40 - 1000 times  
start_time = time.time()
for i in range(1001):
  num = random.randrange(41)
  print('using cache, what is the Fibonacci number of %d?'% num)
  print (fibonacciResults[num])
secondLenghtTime = time.time() - start_time 
print("---it took %f seconds to execute the formula---" % (firstLenghtTime))
print("---it took %f seconds to execute with the cache---" % (secondLenghtTime))