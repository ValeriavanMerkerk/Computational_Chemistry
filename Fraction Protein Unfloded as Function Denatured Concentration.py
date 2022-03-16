# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 20:08:51 2020

@author: Valeria van Merkerk
"""
#computational hw on Protein Denaturation
#input data to model a graph with data points


data="""0.5	0.114822008
1	0.142325463
1.5	0.187815943
2	0.238022307
2.5	0.290052484
3	0.353114837
3.5	0.425365439
4	0.502
4.5	0.576634561
5	0.650885163
5.5	0.714947516
6	0.776977693
6.5	0.831184057
7	0.862674537
7.5	0.896177992
8	0.929755112
8.5	0.947568057
9	0.954729847
9.5	0.972224435
10	0.976877221""".split('\n')

Clist=[]
Flist=[]
for s in data:
    if s:
        C,F= s.split()
        C= float(C)
        F= float(F)
        Clist.append(C)
        Flist.append(F)
        
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from numpy import exp

def ProtFoldModel (C,m,Cm):
    return (exp(-m*(Cm-C)/2460))/(1+exp(-m*(Cm-C)/2460))

init_guess=[3400,2.5]
popt, pcov= curve_fit(ProtFoldModel, Clist, Flist, init_guess)

print(popt, pcov)
plt.scatter (Clist, Flist, label='data')
plt.plot (Clist,ProtFoldModel(Clist, *popt), label= 'fit'+ 'm='+str(popt[0])+'Cm='+str(popt[1]))
plt.title ('Fraction Protein Unfolded as Function of Denaturant Concentration')
plt.xlabel('C(M)')
plt.ylabel('F')
plt.legend()
