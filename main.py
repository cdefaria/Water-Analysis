#!/usr/bin/env python
import math
#import print_function 
from . import graph
from . import node
#import topSort.py


#filename = input("What file do you want to use?\n")
endpoint = input("What sensor do you want to be the end point?\n")


cur=org=nodes[int(endpoint)]
while cur.m_checked==0 and next(cur.m_id):
    if cur.m_id == endpoint:
        cur.m_percent = 1
        cur.m_through=sum_in(cur.m_id)
        cur.m_org=sum_out(cur.m_id)-sum_in(cur.m_id)
    else:
        cur.m_percent=sumTo(cur.m_id, endpoint)/sum_in(cur.m_id)
        cur.m_through=sum_out(cur.m_id)*cur.m_percent
        cur.m_org=(sum_out(cur.m_id)-sum_in(cur.m_id))*cur.m_through
    cur.check()
    cur=nodes[next(cur)]

print("Model 1:")
for i in range(1,9):
    percent=str(nodes[i].m_percent*100)+"% "
    #if(i%3):
    #    print(percent,end='')
    #else:
    print(percent)

print("Model 2:")
for i in range(1,9):
    through=str(nodes[i].m_through)+" "
    #if(i%3):
    #    print(through,end='')
    #else:
    print(through)

print("Model 3:")
for i in range(1,9):
    origin=str(nodes[i].m_org)+" "
    #if(i%3):
    #    print(origin,end='')
    #else:
    print(origin)
