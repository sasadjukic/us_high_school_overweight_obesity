
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

def get_states_overweight_or_obesity_crude_2021(ob: pd.DataFrame) -> pd.DataFrame:

    # get states with relevant column data for 2021
    states = ob[
                    (ob['stratification1'] == 'Overall') &
                    (ob['datavaluetype'] == 'Crude Prevalence') &
                    (ob['yearstart'] == 2021)
                ]

    # no data on Florida for 2021 so remove FL
    states_sans_florida = states.loc[statewide['locationabbr'] != 'FL']

    return states_sans_florida

def get_top_15_overweight_or_obese_states(so_2021: pd.DataFrame) -> pd.DataFrame:

    # top 15 states with highest overwaeight/obesity rates
    return so_2021[['locationabbr', 'datavaluealt']].nlargest(15, columns='datavaluealt')

states_overweight_or_obesity = get_states_only(overweight_or_obesity_main)
overweight_or_obesity = get_overweight_or_obesity_value_columns(states_overweight_or_obesity)
states_overweight_or_obesity_2021 = get_states_overweight_or_obesity_crude_2021(overweight_or_obesity)
top_15 = get_top_15_overweight_or_obese_states(states_overweight_or_obesity_2021)