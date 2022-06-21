import pyam as py
import matplotlib.pyplot as plt
import os

plt.style.use("ggplot")

fig, ax = plt.subplots()
df = py.IamDataFrame("hourly_values.xlsx")
df.plot(
    color="variable",
    title="Electricity day-ahead and future prices in EUR/MWh",
    marker="d",
    markersize=0,
    ax=ax,
    linewidth=1
)

Lines = ax.get_lines()


Lines[0].set_color('#00CC66')
Lines[1].set_color('black')
Lines[1].set_linestyle('dashed')
Lines[1].set_linewidth(1.5)
Lines[2].set_color('#FF8000')
Lines[2].set_linewidth(1.5)





plt.xlabel("Time in h")
plt.ylabel("")
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
legend = plt.legend(fontsize=12, loc='upper left')
legend.get_texts()[0].set_text("Day-Ahead (EPEX)")
legend.get_texts()[1].set_text("Average day-ahead (EPEX) (41.2 EUR/MWh)")
legend.get_texts()[2].set_text("Future contract (EEX) (45 EUR/MWh)")

plt.tight_layout()
fig.savefig("hourly_values.png", dpi=500)
fig.savefig("hourly_values.eps", dpi=500)