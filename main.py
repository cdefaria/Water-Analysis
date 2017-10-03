#!/usr/bin/env python
import math
#import print_function 
#from . import graph
#import topSort.py

class Node:
    m_id=""
    m_percent=0
    m_through=0
    m_orig=0
    m_checked=0
    def __init__(self, idValue):
        self.m_id=idValue
    def check(self):
        self.m_checked=1

nodes=[]

for i in range(1,10):
    nodes.append(Node(i))

g = {'1':{'2':-5, '4':-5}, '2':{'1':5, '3':-2, '5':-3}, '3':{'2':2}, '4':{'1':5}, '5':{'2':3, '6':-8, '8':-2}, '6':{'5':8, '9':-3}, '8':{'5':2, '9':-2},  '9':{'6':3, '8':2}}

def next(c):
    #print(g[c])
    for key,value in g[c].items():
        if value > 0:
            if nodes[int(key)].m_checked == 0:
                return key
    return 0

def sumTo(start, end):
    sum=0
    nodes[int(start)].check()
    for key,value in g[start].items():
        if value > 0:
            if key == end:
                return value
            elif nodes[start].m_checked == 0:
                sum+=sumTo(key,end)
            else:
                return 0
    return sum

def sum_in(id):
    sum=0
    for key,value in g[id].items():
        if value >= 0:
            sum+=value
    return sum

def sum_out(id):
    sum=0
    for key,value in g[id].items():
        if value < 0:
            sum-=value
    return sum

#filename = input("What file do you want to use?\n")
endpoint = input("What sensor do you want to be the end point?\n")


cur=org=nodes[int(endpoint)]
while cur.m_checked==0 and next(str(cur.m_id)):
    if cur.m_id == endpoint:
        cur.m_percent = 1
        cur.m_through=sum_in(str(cur.m_id))
        cur.m_orig=sum_out(str(cur.m_id))-sum_in(str(cur.m_id))
    else:
        cur.m_percent=sumTo(str(cur.m_id), endpoint)/sum_in(str(cur.m_id))
        cur.m_through=sum_out(str(cur.m_id))*cur.m_percent
        cur.m_orig=(sum_out(str(cur.m_id))-sum_in(str(cur.m_id)))*cur.m_through
    cur.check()
    cur=nodes[int(next(str(cur.m_id)))]

print("Model 1:")
for i in nodes:
    percent=str(i.m_percent*100)+"% "
    if(i.m_id%3):
        print(percent,end='')
    else:
        print(percent)

print("Model 2:")
for i in nodes:
    through=str(i.m_through)+" "
    if(i.m_id%3):
        print(through,end='')
    else:
        print(through)

print("Model 3:")
for i in nodes:
    origin=str(i.m_orig)+" "
    if(i.m_id%3):
        print(origin,end='')
    else:
        print(origin)
