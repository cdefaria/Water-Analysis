#!/usr/bin/env python3

import numpy as np
import flopy

modelname = 'tutorial1'
mf = flopy.modflow.Modflow(modelname, exe_name='./mf2005')

Lx = 1000.
Ly = 1000.
ztop = 0.
zbot = -50.
nlay = 1
nrow = 10
ncol = 10
delr = Lx/ncol
delc = Ly/nrow
delv = (ztop - zbot) / nlay
botm = np.linspace(ztop, zbot, nlay + 1)

dis = flopy.modflow.ModflowDis(mf, nlay, nrow, ncol, delr=delr, delc=delc,
                                       top=ztop, botm=botm[1:])

ibound = np.ones((nlay, nrow, ncol), dtype=np.int32)
ibound[:, :, 0] = -1
ibound[:, :, -1] = -1
strt = np.ones((nlay, nrow, ncol), dtype=np.float32)
strt[:, :, 0] = 10.
strt[:, :, -1] = np.linspace(10,0,10) 
strt[:, 8:10, -1] = 2.
strt[:, -1, 4:6] = 1.
bas = flopy.modflow.ModflowBas(mf, ibound=ibound, strt=strt)

lpf = flopy.modflow.ModflowLpf(mf, hk=10., vka=10.)

spd = {(0, 0): ['print head', 'print budget', 'save head', 'save budget']}
oc = flopy.modflow.ModflowOc(mf, stress_period_data=spd, compact=True)

pcg = flopy.modflow.ModflowPcg(mf)

mf.write_input()

success, buff = mf.run_model()

import matplotlib.pyplot as plt
import flopy.utils.binaryfile as bf

hds = bf.HeadFile(modelname+'.hds')
times = hds.get_times()
head = hds.get_data(totim=times[-1])
levels = np.linspace(0, 10, 11)

cbb = bf.CellBudgetFile(modelname+'.cbc')
kstpkper_list = cbb.get_kstpkper()
frf = cbb.get_data(text='FLOW RIGHT FACE', totim=times[-1])[0]
right=open("frf.txt", 'w')
right.write(', '.join([str(x) for x in frf]))
fff = cbb.get_data(text='FLOW FRONT FACE', totim=times[-1])[0]
front=open("fff.txt", 'w')
front.write(', '.join([str(x) for x in fff]))
