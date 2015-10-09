#!/usr/bin/python
import math

Max=10000

cubeSet=set()

upperLimit=int(Max**1./3)+2

for n in xrange(1,upperLimit):
    cubeSet.add(n*n*n)

for m in xrange(1,Max+1):
    for n in cubeSet:
        k=m-n
        if k in cubeSet and k<=n:
            print m,"=",n,"+",k
