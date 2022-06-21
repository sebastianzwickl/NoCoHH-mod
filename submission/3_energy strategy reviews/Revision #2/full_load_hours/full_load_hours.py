import pyam
import matplotlib.pyplot as plt

from matplotlib import rc

rc('text', usetex=True)



fig = plt.figure(constrained_layout=False)
plt.style.use('ggplot')

plt.rcParams['xtick.labelsize'] = 12
plt.rcParams['ytick.labelsize'] = 12
gs = fig.add_gridspec(1, 2)

fig_base = fig.add_subplot(gs[0, 0])
fig_low = fig.add_subplot(gs[0, 1])

# read in data from IAMC format
data = pyam.IamDataFrame('full_load_hours.xlsx')

data.filter(scenario='Base').plot(ax=fig_base, legend=False, color='variable', linewidth=2, marker='d', markersize=3.5)
lines = fig_base.get_lines()
lines[0].set_color('#00CC66')
lines[1].set_color('#FF8000')
lines[2].set_color('#0080FF')




fig_base.set_title(r'$p_{t}^{CO_2}=100\,\frac{EUR}{t}$', fontsize=12)


data.filter(scenario='Low').plot(ax=fig_low, legend=True, color='variable', linewidth=2, marker='d', markersize=3.5)
fig_low.set_title(r'$p_{t}^{CO_2}=150\,\frac{EUR}{t}$', fontsize=12)
lines = fig_low.get_lines()
lines[0].set_color('#00CC66')
lines[1].set_color('#FF8000')
lines[2].set_color('#0080FF')

leg = fig_low.legend()
lines = leg.get_lines()
lines[0].set_color('#00CC66')
lines[1].set_color('#FF8000')
lines[2].set_color('#0080FF')

fig_low.set_xlabel(r'Future contract price in $\frac{EUR}{MWh}$', fontsize=12)
fig_base.set_xlabel(r'Future contract price in $\frac{EUR}{MWh}$', fontsize=12)



fig_base.set_ylabel('')

fig.suptitle('Share on revenues in \% for different future contract prices $p_t^{future}$', fontsize=14, y=0.975)
plt.tight_layout()

plt.savefig('future_sensitivities.png', dpi=1000)


