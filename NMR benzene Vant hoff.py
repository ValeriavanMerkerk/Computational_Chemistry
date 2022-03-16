# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 13:11:30 2022

@author: valer
"""


from scipy import stats

import numpy as np

import matplotlib.pyplot as plt

x= np.array ([0.003413,0.00330033,0.003195,0.003095975,0.003003003])
y= np.array ([2.199444,2.263844,2.186051,2.129897,2.095438])

plt.plot (x,y,'o')

m,b = np.polyfit(x,y,1)

slope, intercept, r_value, p_value,std_err = stats.linregress (x,y)
print ("slope: %f intercept: %f" % (slope, intercept))
print("R-squared: %f" % r_value **2)

Enthalpy =(-slope*0.00083145)
print( "Enthalpy ="+str(Enthalpy))

Entropy = (intercept*8.3145)
print("Entropy="+str (Entropy))

plt.plot(x,m*x+b)
plt.xlabel('1/T')
plt.ylabel('ln(Keq)')
plt.title ("Van'T Hoff plot"+ " R-squared:%f" %r_value**2)

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

green_patch = mpatches.Patch(color='green', label ="Entropy="+str (Entropy))
pink_patch = mpatches.Patch(color='pink', label ="Entalpy="+str (Enthalpy))
orange_patch=mpatches.Patch(color='orange', label ="y="+str (slope)+"x"+"+"+str(intercept))
plt.legend(handles=[green_patch, pink_patch, orange_patch])

plt.show()
