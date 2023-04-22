
import pandas as pd
from overweight_or_obesity_nationwide import overweight_or_obesity_main  

def get_states_only(ob: pd.DataFrame) -> pd.DataFrame:

    # remove all non USA states from dataframe
    nob = ob.loc[
                (ob['locationdesc'] != 'United States') &
                (ob['locationdesc'] != 'Puerto Rico') &
                (ob['locationdesc'] != 'Guam') &
                (ob['locationdesc'] != 'Virgin Islands')
            ]

    return nob

def get_overweight_or_obesity_value_columns(main: pd.DataFrame) -> pd.DataFrame:

    # keep only relevant columns 
    overweight_or_obesity = main[['yearstart', 'locationabbr', 'datavaluealt',  'stratification1', 'datavaluetype']]
    return overweight_or_obesity

def get_states_overweight_or_obesity_crude_2011(ob: pd.DataFrame) -> pd.DataFrame:

    # get states with relevant column data for 2021
    states = ob[
                    (ob['stratification1'] == 'Overall') &
                    (ob['datavaluetype'] == 'Crude Prevalence') &
                    (ob['yearstart'] == 2011)
    ]

    return states 

def get_2011_rates_for_top_15_2021_states(so_2011: pd.DataFrame) -> dict[str:int]:

    ''' 
        get 2011 crude rates for top 15 states from 2021 (we'll use this to create a comparison chart)
        most of the 2011 top 15 and 2021 top 15 match but few states made top 15 in 2011 and did not in 2021
    '''

    top_15_2021 = [
                    'WV', 'MS', 'KY', 'SD', 'OK', 
                    'AL', 'TN', 'OH', 'LA', 'NE',
                    'IA', 'KS', 'SC', 'AR', 'ND'
                    ]

    top_15_2021_in_2011 = {}

    for i in so_2011.index:
        state = so_2011.loc[i, 'locationabbr']
        o_rate = so_2011.loc[i, 'datavaluealt']
        if state in top_15_2021:
            top_15_2021_in_2011[state] = o_rate

    return top_15_2021_in_2011

states_overweight_or_obesity = get_states_only(overweight_or_obesity_main)
overweight_or_obesity = get_overweight_or_obesity_value_columns(states_overweight_or_obesity)
states_overweight_or_obesity_2011 = get_states_overweight_or_obesity_crude_2011(overweight_or_obesity)
rates_2011 = get_2011_rates_for_top_15_2021_states(states_overweight_or_obesity_2011)



