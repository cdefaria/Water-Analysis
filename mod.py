#!/usr/bin/env python3


nrow = 3
ncol = 3
frf = [-5, -5, -10, -5, -8, 0, 0, 0, 0]
right=open("frf.txt", 'w')
right.write(', '.join([str(x) for x in frf]))
fff = [0, -5, 10, -5, -5, 5, 0, -2, -1]
front=open("fff.txt", 'w')
front.write(', '.join([str(x) for x in fff]))
