
'''
    get percentage of obesity among students in high school
    will export some of the data to our three state comparison module
    the bottom 3 will help choose state to use for three state comparison
    the top 3 will be used for a different chart
'''

import pandas as pd 
from usa_health_main import usa_main
from hs_health_helper import get_value_columns, get_states_crude_prevelance_2019, get_us_states_only

def get_obesity_main(data: pd.DataFrame) -> pd.DataFrame:
    '''get the right survey question for our dataframe'''
    ob_main = data[data['question'] == 'Obesity among high school students']
    return ob_main

def get_top_3_states_hs_obesity(hso_2019: pd.DataFrame) -> pd.DataFrame:
    '''get dataframe with top 3 states in high school obesity'''
    return hso_2019.nlargest(3, columns='datavaluealt')

def get_bottom_3_states_hs_obesity(hso_2019: pd.DataFrame) -> pd.DataFrame:
    '''get dataframe with bottom 3 states in high school obesity'''
    return hso_2019.nsmallest(3, columns='datavaluealt')

def get_hs_obesity_ranks_2019(hso_2019: pd.DataFrame) -> pd.DataFrame:
    '''get obesity rankings of all 50 states + DC'''
    return hso_2019.nlargest(51, columns='datavaluealt')

obesity = get_obesity_main(usa_main)
ob_states_only = get_us_states_only(obesity)
ob_value_columns = get_value_columns(ob_states_only)
ob_sto_2019 = get_states_crude_prevelance_2019(ob_value_columns)
top_3_states = get_top_3_states_hs_obesity(ob_sto_2019)
bottom_3_states = get_bottom_3_states_hs_obesity(ob_sto_2019)
rankings = get_hs_obesity_ranks_2019(ob_sto_2019)


