

# I ENDED UP NOT USING DATA FROM THIS MODULE
'''
    get percentage of high school students meeting aerobic physical activity guidlines
    will export data to our three state comparison module
'''

import pandas as pd
from usa_health_main import usa_main
from hs_health_helper import get_value_columns, get_states_crude_prevelance_2019

def get_aero_phys_activity_2019(data: pd.DataFrame) -> pd.DataFrame:

    '''get the right survey question for our dataframe'''
    ppe = data[data['question'] == 'Meeting aerobic physical activity guidelines among high school students']
    return ppe

apa_2019 = get_aero_phys_activity_2019(usa_main)
apa_columns = get_value_columns(apa_2019)
apa_states_2019 = get_states_crude_prevelance_2019(apa_columns)