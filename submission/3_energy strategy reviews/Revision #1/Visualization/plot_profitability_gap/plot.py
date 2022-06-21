import pyam
import pandas as pd
import matplotlib.pyplot as plt


df_shadow = pyam.IamDataFrame('IAMC_Profitability_Gap.xlsx')
# df_prices = pyam.IamDataFrame('IAMC_inputs.xlsx')


def find_profitability_edge(data_prices):
    _future = data_prices.filter(variable='Future contract').data.value[0]
    return _future


def return_new_prices(df_prices):
    _spot = df_prices.filter(variable='Day-Ahead').data['value'].values
    _future = find_profitability_edge(df_prices)
    _p = []
    for _s in _spot:
        if 2*_s > 2*_future:
            _p.append(2*_future)
        else:
            _p.append(2*_s)
    return _p
    
# _val = return_new_prices(df_prices)

def write_IAMC(output_df, model, scenario, region, variable, unit, time, values):
    
    if isinstance(values, list):
        _df=pd.DataFrame({'model': model,
                      'scenario': scenario,
                      'region': region,
                      'variable': variable,
                      'unit': unit,
                      'year': time,
                      'value': values})
    else:
        _df=pd.DataFrame({'model': model,
                     'scenario': scenario,
                     'region': region,
                     'variable': variable,
                     'unit': unit,
                     'year': time,
                     'value': values}, index=[0])
        
    output_df = output_df.append(_df)
    return output_df

output_iamc = pd.DataFrame()
_scenario = 'Baseline'
_model = 'NoCopHH-modv1.0'
_region = 'Norway'
_unit = 'EUR'
_time = list(_t for _t in range(1, 49, 1))
output_iamc = pd.DataFrame()

# output_iamc = write_IAMC(output_iamc, _model, _scenario, _region, 'Opportunity costs', _unit, _time, _val)
output_iamc = output_iamc.append(df_shadow.as_pandas()).drop(columns='exclude')
output_iamc = pyam.IamDataFrame(output_iamc)

plt.style.use('ggplot')
fig, ax = plt.subplots()
output_iamc.plot(color='variable', title='Resource opportunity costs (OC) in EUR/MWh', marker="d", markersize=5, ax=ax, cmap='Accent', legend=True)
plt.title('Resource opportunity costs (OC) in EUR/MWh', fontsize=12)


lines = ax.get_lines()
lines[2].set_linewidth(2)
lines[2].set_markersize(0)
lines[2].set_linestyle('dashed')


plt.xlabel('Time in h')
plt.ylabel('')
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
legend = plt.legend(fontsize=10, bbox_to_anchor=(1, 0.5))

legend.get_texts()[0].set_text('$OC_{Day-Ahead}$')
legend.get_texts()[1].set_text('$OC_{Future~contract}$')
legend.get_texts()[2].set_text('Profitability limit')


plt.tight_layout()
fig.savefig('Profitability gap.png', dpi=500)

