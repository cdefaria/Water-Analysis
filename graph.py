#!/usr/bin/env python
#import node.py

g = {'1':{'2':-5, '4':-5}. '2':{'1':5, '3':-2, '5':-3}, '3':{'2':2}, '4':{'1':5}, '5':{'2':3, '6':-8, '8':-2}, '6':{'5':8, '9':-3}, '8':{'5':2, '9':-2}  '9':{'6':3, '8':2}}

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
