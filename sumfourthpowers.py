#!/usr/bin/python
import math

Max=10000

fourthPowerSet=set()

upperLimit=int(Max**1./4)+2

for n in xrange(1,upperLimit):
    fourthPowerSet.add(n*n*n*n)

for m in xrange(1,Max+1):
    for n in fourthPowerSet:
        k=m-n
        if k in fourthPowerSet and k<=n:
            print m,"=",n,"+",k
