
''' 
    Comparing three states (highest_obesity, lowest_obesity, random state in the middle)
    and few other avaliable catogeries for year 2019 (last year to have comprehensive data)
    to get a clearer picture of perhaps why things are the way they are with high school students
    States in question ended up being West Virginia(highest obesity), Hawaii(2nd lowest obesity), California(average) 
    New Jersey and New Hempshire (tied at 1st for lowest obesity) that reported a tad bit lower obesity than Hawaii for 2019 do have missing values in other categories
''' 

import pandas as pd
from hs_healthy_weight_students_2019 import hw_statewide_2019
from hs_overweight_or_obesity_states_2019 import oob_sto_2019
from hs_obesity_states_2019 import ob_sto_2019
from hs_participation_physical_edu_states_2019 import ppe_states_2019
from hs_meeting_aerobic_physical_activity_guidelines_states_2019 import apa_states_2019
from state_poverty_rates import poverty_states_2019

def get_three_states_data_2019(data: pd.DataFrame) -> pd.DataFrame:
    '''
        run data frame through a for loop to get the numbers for our three states
    '''

    tri_state = {}

    for i in data.index:
        states = ['WV', 'HI', 'CA']
        location = data.loc[i, 'locationabbr']
        value = data.loc[i, 'datavaluealt']
        if location in states:
            tri_state[location] = value

    return tri_state 


# call the function with different data to get three state numbers 
healthy_weight = get_three_states_data_2019(hw_states_2019)
overweight_obesity = get_three_states_data_2019(oob_sto_2019)
obesity = get_three_states_data_2019(ob_sto_2019)
hs_ppe = get_three_states_data_2019(ppe_states_2019)
hs_apa = get_three_states_data_2019(apa_states_2019)
poverty = get_three_states_data_2019(poverty_states_2019)











