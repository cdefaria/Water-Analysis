#!/usr/bin/env python3
from random import *
test=input("Enter the file name of of the model you plan to use:\n")
row=int(input("Enter the number of rows:\n"))
col=int(input("Enter the number of  columns:\n"))
size = col*row
f=open(test, 'w')
f.write("#!/usr/bin/env python3\n")
f.write("nrow = ")
f.write(str(row))
f.write("\nncol = ")
f.write(str(col))
f.write("\nfrf = [")
for i in range(size):
    index = str(randint(0, 10))
    if size != i+1:
        index += ", "
    f.write(index)
f.write("]\n")
f.write("fff = [")
for i in range(size):
    index = str(randint(0, 10)*-1)
    if size != i+1:
        index+=", "
    f.write(index)
f.write("]\n")
f.close
