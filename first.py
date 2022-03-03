import math
import random
import time
start_time = time.time()
fiveSquare = math.sqrt(5)

for i in range(1001):
  num = random.randrange(1,41)
  print('what is the Fibonacci number of %d?'% num)
  result = (1/fiveSquare)*(((1 + fiveSquare)/2)**num - ((1 - fiveSquare)/2)**num)
  print (round(result))
print("---it took %s seconds to be executed---" % (time.time() - start_time))

for i in range(41):
  num = i
  print('the Fibonacci number of %d'% num)
  result = (1/fiveSquare)*(((1 + fiveSquare)/2)**num - ((1 - fiveSquare)/2)**num)
  print (round(result))