#!/usr/bin/python
import math

Max=10000

squareSet=set()

for n in xrange(1,int(math.sqrt(Max)+1)):
    squareSet.add(n*n)

for m in xrange(1,Max+1):
    for n in squareSet:
        k=m-n
        if k in squareSet and k<n:
            print m,"=",n,"+",k
