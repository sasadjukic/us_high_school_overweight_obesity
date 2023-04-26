
# I ENDED UP NOT USING DATA FROM THIS MODULE
'''
    get percentage of high school students participating in daily physical education classes
    will export data to our three state comparison module
'''

import pandas as pd
from usa_health_main import usa_main
from hs_health_helper import get_value_columns, get_states_crude_prevelance_2019

def get_part_phys_edu_2019(data: pd.DataFrame) -> pd.DataFrame:

    '''get the right survey question for our dataframe'''
    ppe = data[data['question'] == 'Participation in daily school physical education classes among high school students']
    return ppe

ppe_2019 = get_part_phys_edu_2019(usa_main)
ppe_columns = get_value_columns(ppe_2019)
ppe_states_2019 = get_states_crude_prevelance_2019(ppe_columns)