# -*- coding: utf-8 -*-
"""
Created on Wed May 12 09:29:29 2021

@author: zwickl-nb
"""

import pyam
import matplotlib.pyplot as plt
import matplotlib.ticker as tkr

from matplotlib import rc

rc('text', usetex=True)
plt.rcParams["figure.figsize"] = (16,9)
plt.style.use('ggplot')
fs = 30
fig = plt.figure()
data = pyam.IamDataFrame('full_load_hours.xlsx')
data.plot(color='scenario', linewidth=3, marker='d', markersize=6, cmap='Dark2')
legend = plt.legend(loc='upper left', fontsize=fs)
legend.get_texts()[0].set_text('$p_{t}^{spot}$')
legend.get_texts()[1].set_text(r'$+~0.050~\frac{EUR}{MWh}$')
legend.get_texts()[2].set_text(r'$+~0.125~\frac{EUR}{MWh}$')
legend.get_texts()[3].set_text(r'$+~0.250~\frac{EUR}{MWh}$')


plt.xticks(fontsize=fs)
plt.yticks(fontsize=fs)
plt.xlabel('$CO_2$ price in EUR/t', fontsize=fs)

group_thousands = tkr.FuncFormatter(lambda x, pos: '{:0,d}'.format(int(x)).replace(',', ' '))
plt.gca().xaxis.set_major_formatter(group_thousands)

plt.gca().yaxis.set_major_formatter(group_thousands)


plt.title('$H_2$ annual full-load production hours for different $p_t^{spot}$ increases', fontsize=fs+4)

plt.text(202, 2250,"(a)", color='black', fontsize=28)
plt.text(202, 1580,"(b)", color='black', fontsize=28)
plt.text(202, 450,"(c)", color='black', fontsize=28)
plt.text(202, 10,"(d)", color='black', fontsize=28)
plt.tight_layout()


plt.savefig('Full_load_hours1.png', dpi=1000)
# plt.savefig('Full_load_hours1.eps', dpi=500)