#!/usr/bin/env python
import graph.py
import node.py
#import topSort.py



filename = input("What file do you want to use?\n")
endpoint = input("What sensor do you want to be the end point?\n")

cur=org=nodes[endpoint]
while !cur.checked && next(cur.m_id):
    if cur.m_id == endpoint:
        cur.m_percent = 1
        cur.m_through=sum_in(cur.m_id)
        cur.m_org=sum_out(cur.m_id)-sum_in(cur.m_id)
    else:
        cur.m_percent=sumTo(cur.m_id, endpoint)/sum_in(cur.m_id)
        cur.m_through=sum_out(cur.m_id)*cur.percent
        cur.m_org=(sum_out(cur.m_id)-sum_in(cur.m_id))*cur.through
    cur.check()
    cur=nodes[next(cur)]
