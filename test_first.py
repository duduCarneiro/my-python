import pytest
from first import FromFormula, NthFibonacci
from first import FromCache


def testOnCache():
  testArgumentNumber = 6
  expected = 8
  actual = FromCache(testArgumentNumber)
  message = "blablablaa %d" % (expected)
  assert actual == expected, message
  
  
def testOnCache2():
  testArgumentNumber = 40
  expected = 102334155
  actual = FromCache(testArgumentNumber)
  message = 'testando'
  assert actual == expected, message
  
def testOnFormula():
  testArgumentNumber = 40
  expected = 102334155
  actual = FromFormula(testArgumentNumber)
  message ='test'
  assert actual == expected, message