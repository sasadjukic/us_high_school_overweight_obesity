
# I ENDED UP NOT USING DATA FROM THIS MODULE
'''
    get percentage of population living in poverty
    will export data to our three state comparison module
'''

import pandas as pd
from usa_health_main import usa_main
from hs_health_helper import get_value_columns, get_states_crude_prevelance_2019

def get_poverty_2019(data: pd.DataFrame) -> pd.DataFrame:

    '''get the right survey question for our dataframe'''
    ppe = data[data['question'] == 'Poverty']
    return ppe

poverty_2019 = get_poverty_2019(usa_main)
poverty_columns = get_value_columns(poverty_2019)
poverty_states_2019 = get_states_crude_prevelance_2019(poverty_columns)