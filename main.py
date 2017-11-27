#!/usr/bin/env python
import math
#import tkinter
import tkinter as tk
#from Tkinter import *
#from modules.logic import game
#import options
import random
import os
#importlib
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
rows = 3
col = 3

for i in range(1,10):
    nodes.append(Node(str(i)))

#nodes.append(0)

g = {'1':{'2':-5, '4':-5}, '2':{'1':5, '3':-5, '5':-5}, '3':{'2':5, '6':5}, '4':{'1':5, '5':-5}, '5':{'2':5, '4':5, '6':-8, '8':-2}, '6':{'3':-5, '5':8, '9':-1}, '8':{'5':2},  '9':{'6':1}}

#def next(c):
#    if nodes[c] and str(c+1) in g.keys():
#        return int(c+1)
#    return 0

def sumTo(start, end):
    sum=0
    for key,value in g[start].items():
        if int(key) <= 0:
            return 0
        if value > 0:
            if key == end:
                return value
            else:
                sum+=(value+sumTo(key,end))
    return sum

def sum_in(id):
    sum=0
    for key,value in g[id].items():
        if int(key) <= 0:
            return 0
        if value < 0:
            sum+=abs(value)
    return sum

def sum_out(id):
    sum=0
    for key,value in g[id].items():
        if int(key) <= 0:
            return 0
        if value > 0:
            sum+=abs(value)
    return sum

def model_data():
    endpoint = input("What block do you want to be the end point?\n")

    cur=nodes[int(endpoint)-1]
    while cur.m_checked==0 and int(cur.m_id) <= len(nodes):
        sIn=sum_in(str(cur.m_id))
        sOut=sum_out(str(cur.m_id))
        sTo=sumTo(str(cur.m_id), endpoint)
        if str(cur.m_id) == str(endpoint):
            cur.m_percent = 1
            cur.m_through=sIn
            if sOut>sIn:
                cur.m_orig=sOut-sIn
            else:
                cur.m_orig=0
        else:
            if sIn:
                cur.m_percent=sTo/sIn
            else:
                cur.m_percent=0
                cur.m_through=sIn*cur.m_percent
            if sOut>sIn:
                cur.m_orig=sOut-sIn*cur.m_percent
            else:
                cur.m_orig=0
        cur.check()
        if len(nodes) > int(cur.m_id):
            cur=nodes[int(cur.m_id)]
        else:
            return

def print_models():
    print("Model 1:")
    for i in nodes:
        percent=str(i.m_percent*100)+"% "
        if(int(i.m_id)%3):
            print(percent, end='')
        else:
            print(percent)
    print("Model 2:")
    for i in nodes:
        through=str(i.m_through)+" "
        if(int(i.m_id)%3):
            print(through, end='')
        else:
            print(through)
    print("Model 3:")
    for i in nodes:
        origin=str(i.m_orig)+" "
        if(int(i.m_id)%3):
            print(origin, end='')
        else:
            print(origin)

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.canvas = tk.Canvas(self, width=500, height=500, borderwidth=0, highlightthickness=0)
        self.canvas.pack(side="top", fill="both", expand="true")
        self.rows = rows
        self.columns = cols
        self.cellwidth = 10
        self.cellheight = 10
        self.rect = {}
        for column in range(cols):
            for row in range(rows):
                x1 = column*self.cellwidth
                y1 = row * self.cellheight
                x2 = x1 + self.cellwidth
                y2 = y1 + self.cellheight
                color = hex(nodes[column+row].through)
                self.rect[row,column] = self.canvas.create_rectangle(x1,y1,x2,y2, fill="blue", tags="rect")

#myapp = App()

#myapp.master.title("Modeflow Output Window")
#myapp.master.maxsize(11*rows, 12*col)

userFile = ""
while userFile != "Y" and userFile != "N":
    userFile = input("Do you want to use your own Modflow model? (Y/N)")
    userFile=userFile.upper()
    if userFile != "Y" and userFile != "N":
        print("Invalid Input\n")

modFile=""
if userFile == "Y":
    modFile=input("Enter the file name of of the model you plan to use:\n")
    #importlib.import_module(modFile)
    #print(frf)
    f=open(modFile, 'r')
    exe=open("mod.py", 'w')
    exe.write("#!/usr/bin/env python3\n")
    exe.write("\n")
    for line in f:
        if line[:1] == "#" or line[:3] == "fig" or line[:2] == "ax":
            continue
        if line == "mf = flopy.modflow.Modflow(modelname, exe_name=\'../mf2005\')":
            exe.write("mf = flopy.modflow.Modflow(modelname, exe_name='./mf2005')")
            continue
        exe.write(line)
        if line[:3] == "frf":
            exe.write("right=open(\"frf.txt\", \'w\')\n")
            exe.write("right.write(\', \'.join([str(x) for x in frf]))\n")
        if line[:3] == "fff":
            exe.write("front=open(\"fff.txt\", \'w\')\n")
            exe.write("front.write(\', \'.join([str(x) for x in fff]))\n")
            exe.close()
            break
        if line[:4] == "nrow":
            rows = int(line[7:])
        if line[:4] == "ncol":
            cols = int(line[7:])
    os.system('./bash.sh')

if userFile == "Y":
    fff = open("fff.txt", 'r')
    frf = open("frf.txt", 'r')
    nodes = []
    g = {}
    g.update({"0":{}})
    g.update({"-1":{}})
    for fff_data in fff:
        fff_list = fff_data.split(", ")
        for i in range(len(fff_list)):
            g.update({str(i+1):{}})
        frf_data = frf.readline()
        frf_list = frf_data.split(", ")
        for i in range(len(fff_list)):
            nodes.append(Node(str(i+1)))
            if i+1 == rows:
                g[str(i+1)].update({"0":float(fff_list[i])})
                g["0"].update({str(i+1):-1*float(fff_list[i])})
                g[str(i+1)].update({"-1":float(frf_list[i])})
                g["-1"].update({str(i+1):-1*float(frf_list[i])})
                continue
            if i+1 <= rows:
                g[str(i+1)].update({"0":float(fff_list[i])})
                g["0"].update({str(i+1):-1*float(fff_list[i])})
            else:
                g[str(i+1)].update({str((i+1)-rows):float(fff_list[i])})
                g[str((i+1)-rows)].update({str(i+1):-1*float(fff_list[i])})
            if i+1 % cols and i+2 <= (rows*cols):
                g[str(i+1)].update({str((i+2)):float(frf_list[i])})
                g[str((i+2))].update({str(i+1):-1*float(frf_list[i])})
            else:
                g[str(i+1)].update({"0":float(frf_list[i])})
                g["0"].update({str(i+1):-1*float(frf_list[i])})
        model_data()
        print_models()
        #myapp.mainloop()
else:
    model_data()
    print_models()
    #myapp.mainloop()

