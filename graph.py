#!/usr/bin/env python
#import node.py

g = {}

def next(cur):
    for key,value in g[cur]
        if value > 0
            if nodes[key].m_checked == 0
                return key
    return ""

def sumTo(start, end):
    sum=0
    nodes[start].check()
    for key,value in g[start]
        if value > 0
            if key == end
                return value
            else if nodes[start].m_checked == 0
                sum+=sumTo(key,end)
            else
                return 0
    return sum

def sum_in(id):
    sum=0
    for key,value in g[id]:
        if value >= 0:
            sum+=value
    return sum

def sum_out(id):
    sum=0
    for key,value in g[id]:
        if value < 0:
            sum-=value
    return sum
