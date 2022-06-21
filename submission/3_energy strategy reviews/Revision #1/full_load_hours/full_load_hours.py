import pyam
import matplotlib.pyplot as plt

from matplotlib import rc

rc('text', usetex=True)


fig = plt.figure(constrained_layout=False)
plt.style.use('ggplot')
gs = fig.add_gridspec(1, 4)

fig_base = fig.add_subplot(gs[0, 0])
fig_low = fig.add_subplot(gs[0, 1])
fig_mid = fig.add_subplot(gs[0, 2])
fig_high = fig.add_subplot(gs[0, 3])

# read in data from IAMC format
data = pyam.IamDataFrame('full_load_hours.xlsx')

data.filter(scenario='Base').plot(ax=fig_base, legend=False, color='scenario', linewidth=2, marker='d', markersize=3.5)
fig_base.set_title('$p_{t}^{spot}$', fontsize=10)


data.filter(scenario='Low').plot(ax=fig_low, legend=False, color='scenario', linewidth=2, marker='d', markersize=3.5)
fig_low.set_title(r'$+0.05 \cdot \frac{EUR}{MWh}$', fontsize=10)

data.filter(scenario='Mid').plot(ax=fig_mid, legend=False, color='scenario', linewidth=2, marker='d', markersize=3.5)
fig_mid.set_title(r'$+0.125 \cdot \frac{EUR}{MWh}$', fontsize=10)

data.filter(scenario='High').plot(ax=fig_high, legend=False, color='scenario', linewidth=2, marker='d', markersize=3.5)
fig_high.set_title(r'$+0.25 \cdot \frac{EUR}{MWh}$', fontsize=10)

fig_base.set_ylim(0, 2600)
fig_low.set_ylim(0, 2600)
fig_mid.set_ylim(0, 2600)
fig_high.set_ylim(0, 2600)

fig_base.set_xticks([50, 100, 150,200])
fig_low.set_xticks([50, 100, 150,200])
fig_mid.set_xticks([50, 100, 150,200])
fig_high.set_xticks([50, 100, 150,200])

fig_low.set_xlabel('$CO_{2}$ price \n \n (b)', fontsize=10)
fig_mid.set_xlabel('$CO_{2}$ price \n \n (c)', fontsize=10)
fig_high.set_xlabel('$CO_{2}$ price \n \n (d)', fontsize=10)


fig_base.set_ylabel('')
fig_base.set_xlabel('$CO_{2}$ price \n \n (a)', fontsize=10)
fig.suptitle('$H_2$ annual full-load production hours for different $p_t^{spot}$ increases', fontsize=14, y=0.95)
plt.tight_layout()

plt.savefig('Full_load_hours.png', dpi=500)


