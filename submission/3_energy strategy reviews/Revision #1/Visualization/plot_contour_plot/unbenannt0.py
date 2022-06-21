# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 07:29:59 2021

@author: zwickl-nb
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')

_xlist = np.linspace(0, 10, 21)
_ylist = np.linspace(0.5, 0.7, 20)
X, Y = np.meshgrid(_xlist, _ylist)

Z = pd.read_excel('Mappe4.xlsx').to_numpy()

fig,ax=plt.subplots(1,1)
cp = ax.contourf(X, Y, Z, cmap='Blues')

colorbar = fig.colorbar(cp)



 # Add a colorbar to a plot
ax.set_title('$CO_2$ price triggering hydrogen production in EUR/t', pad=15)
#ax.set_xlabel('x (cm)')
ax.set_ylabel('Hydrogen production efficiency')
plt.xticks(fontsize=12)
#plt.xticks([0,1,2,3,4,5,6,7,8,9,10])
plt.yticks(fontsize=12)
ax.set_xlabel('Future contract price increase in %')
plt.tight_layout()
fig.savefig('Contour.png', dpi=500)