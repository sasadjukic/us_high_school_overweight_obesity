

'''
    get percentage of healthy weight students in high school
    will export data to our three state comparison module
'''

import pandas as pd
from usa_health_main import usa_main
from hs_health_helper import get_value_columns, get_states_crude_prevelance_2019

def get_hs_healthy_weight_students(data: pd.DataFrame) -> pd.DataFrame:

    '''get the right survey question for our dataframe'''
    hw_main = data[data['question'] == 'Healthy weight among high school students']
    return hw_main

def get_hs_healthy_weight_rankings_2019(data: pd.DataFrame) -> pd.DataFrame:
    '''get rankings for all 50 states + DC'''
    return data.nlargest(51, columns='datavaluealt')

healthy_weight = get_hs_healthy_weight_students(usa_main)
hw_value_columns = get_value_columns(healthy_weight)
hw_states_2019 = get_states_crude_prevelance_2019(hw_value_columns)
hw_rankings_2019 = get_hs_healthy_weight_rankings_2019(hw_states_2019)




