import math
import random
import time

def NthFibonacci(n):
  fiveSquare = math.sqrt(5)
  return (1/fiveSquare)*(((1 + fiveSquare)/2)**n - ((1 - fiveSquare)/2)**n) #FIXME 

loops = 10000001
maxFibonacci = 40
# applying formula - n from 0 to 40 - 1000 times
start_time = time.time()
for i in range(loops):
  num = random.randrange(maxFibonacci + 1)
  # print('using formula, what is the Fibonacci number of %d?'% num)
  NthFibonacci(num)
firstLenghtTime = time.time() - start_time 
  
  

fibonacciResults = []
for i in range(maxFibonacci + 1):
  fibonacciResults.append(round(NthFibonacci(i)))
  
# caching results - n from 0 to 40 - 1000 times  
start_time = time.time()
for i in range(loops):
  num = random.randrange(maxFibonacci + 1)
  # print('using cache, what is the Fibonacci number of %d?'% num)
  fibonacciResults[num]
secondLenghtTime = time.time() - start_time 
print("---it took %f seconds to execute the formula---" % (firstLenghtTime))
print("---it took %f seconds to execute with the cache---" % (secondLenghtTime))