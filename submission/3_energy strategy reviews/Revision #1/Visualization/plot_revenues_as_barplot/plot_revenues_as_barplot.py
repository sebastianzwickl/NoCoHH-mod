import pyam
import matplotlib.pyplot as plt



# data = pyam.IamDataFrame('costs_development.xlsx')

plt.style.use('ggplot')
# fig, ax = plt.subplots()

# data.plot(color='variable', title='$\lambda_t^{load}$ and future opportunity costs (OC) in EUR/MWh', marker="d", markersize=5, ax=ax, fill_between=False, cmap='tab10')

# lines = ax.get_lines()

# lines[0].set_linestyle('--')
# lines[0].set_markersize(0)
# lines[0].set_color('#9dad7f')
# lines[0].set_linewidth(1.5)
# lines[1].set_markersize(0)
# lines[1].set_linestyle('--')
# lines[1].set_linewidth(1)
# lines[1].set_color('#c7cfb7')
# lines[1].set_linewidth(1.5)

# lines[2].set_color('#ffb26b')
# lines[2].set_linewidth(2)
# lines[3].set_color('#6e7c7c')

# plt.plot([38, 245], [0, 0], color='#ff7b54', linestyle='dotted', linewidth=3)
# plt.plot([245, 245], [0, 90], color='#ff7b54', linestyle='dotted', linewidth=3)
# plt.plot([245, 420], [90, 155.8], color='#ff7b54', linewidth=3)




# ax.text(310, 45,"$p_t^{H_2}=f(CO_2)$", color='#ff7b54', fontsize=12)
# plt.plot([295, 305], [48, 48], color='#ff7b54', linewidth=2)

# legend = ax.get_legend()

# #ff005c


# plt.xlabel('CO$_{2}$ price in EUR/t')
# plt.ylabel('')
# plt.xticks(fontsize=12)
# plt.yticks(fontsize=12)
# plt.xlim([0, 430])

# # plt.legend(fontsize=12)

# legend = plt.gca().legend(fontsize=11, loc='upper left', ncol=2)
# legend.get_texts()[0].set_text('$OC_{future}^{mod}$')
# legend.get_texts()[1].set_text('$OC_{future}^{high}$')
# legend.get_texts()[2].set_text('$OC_{future}^{init}$')
# legend.get_texts()[3].set_text('$\lambda_t^{load}$')



# plt.tight_layout()
# fig.savefig('Break even.png', dpi=500)


fig, ax = plt.subplots()

data_revenues = pyam.IamDataFrame('revenues.xlsx')
barlist = data_revenues.plot.bar(bars='variable', stacked=True, title='Revenues of hydropower plant in thousand EUR', ax=ax)

bars = plt.gca().get_children()
children = barlist.get_children()
children[0].set_color('#a98b98')
children[1].set_color('#a98b98')
children[2].set_color('#a98b98')
children[3].set_color('#a98b98')
children[4].set_color('#a98b98')
children[5].set_color('#a98b98')
children[6].set_color('#a98b98')

children[7].set_color('#8EBAD9')
children[8].set_color('#8EBAD9')
children[9].set_color('#8EBAD9')
children[10].set_color('#8EBAD9')
children[11].set_color('#8EBAD9')
children[12].set_color('#8EBAD9')
children[13].set_color('#8EBAD9')

children[14].set_color('#ff7b54')
children[15].set_color('#ff7b54')
children[16].set_color('#ff7b54')

children[18].set_color('#ff7b54')
children[19].set_color('#ff7b54')
children[20].set_color('#ff7b54')

# print(barlist[0])


plt.xlabel('CO$_{2}$ price in EUR/t')
plt.ylabel('')

plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.legend(fontsize=12)
ax.legend(loc='upper center', ncol=3)
ax.set_ylim([0, 500])
# group_thousands = tkr.FuncFormatter(lambda x, pos: '{:0,d}'.format(int(x)).replace(',', ' '))
# ax.yaxis.set_major_formatter(group_thousands)
plt.xticks(rotation = 45)



plt.tight_layout()
fig.savefig('Revenues.png', dpi=500)