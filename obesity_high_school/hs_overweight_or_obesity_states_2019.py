
'''
    get percentage of overweight or obesity among high school students
    will export some of the data to our three state comparison module
    top 10 from 2013 will be used for another comparison chart
'''

import pandas as pd
from usa_health_main import usa_main
from hs_health_helper import get_value_columns, get_states_crude_prevelance_2019, get_us_states_only

def get_overweight_obesity(data: pd.DataFrame) -> pd.DataFrame:
    '''get the correct survey question for this dataframe'''
    obesity = data[data['question'] == 'Overweight or obesity among high school students']
    return obesity 

def get_top_10_states_2019(oob:pd.DataFrame) -> pd.DataFrame:
    '''get top 10 states with highest high school overweight or obesity for 2019'''
    return oob.nlargest(10, columns='datavaluealt')

def get_hs_oob_rankings_2019(oob: pd.DataFrame) -> pd.DataFrame:
    '''get overweight or obesity rankings for all 50 states + DC'''
    return oob.nlargest(51, columns='datavaluealt')

def get_states_crude_2013(oob: pd.DataFrame) -> pd.DataFrame:
    '''
        get 2013 overweight or obesity numbers for states that ranked in top 10 for 2019
        we'll use this to make comparisons between their numbers for this time span
        2013 is the first year that this data covers   
    '''
    top_10 = [
                'AR', 'MS', 'WV', 'TN', 'AL',
                'GA', 'KY', 'OK', 'DC', 'TX'
            ]

    top_10_2019_in_2013 = {}

    for i in oob.index:
        state = oob.loc[i, 'locationabbr']
        o_rate = oob.loc[i, 'datavaluealt']
        if state in top_10:
            top_10_2019_in_2013[state] = o_rate

    return top_10_2019_in_2013

overweight_obesity = get_overweight_obesity(usa_main)
oob_states_only = get_us_states_only(overweight_obesity)
oob_v_columns = get_value_columns(oob_states_only)
oob_sto_2019 = get_states_crude_prevelance_2019(oob_v_columns)
oob_sto_2013 = get_states_crude_2013(oob_v_columns)
oob_top_10_2019 = get_top_10_states_2019(oob_sto_2019)
oob_rankings_2019 = get_hs_oob_rankings_2019(oob_sto_2019)

