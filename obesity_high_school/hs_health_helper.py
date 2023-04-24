
'''
    across the package we're using same methods to obtain data
    this module stores all the functions we keep reusing again and again
''' 

import pandas as pd 

def get_us_states_only(data: pd.DataFrame) -> pd.DataFrame:
    '''remove all non USA states entries from dataframe'''
    states = data.loc[
                (data['locationdesc'] != 'United States') &
                (data['locationdesc'] != 'Puerto Rico') &
                (data['locationdesc'] != 'Guam') &
                (data['locationdesc'] != 'Virgin Islands')
            ]

    return states

def get_value_columns(data: pd.DataFrame) -> pd.DataFrame:

    '''keep only relevant columns'''
    value_columns = data[['yearstart', 'locationabbr', 'datavaluealt',  'stratification1', 'datavaluetype']]
    return value_columns

def get_states_crude_prevelance_2019(data: pd.DataFrame) -> pd.DataFrame:

    '''get states with relevant column data for 2019 (2019 last year this data covers)'''
    states = data[
                    (data['stratification1'] == 'Overall') &
                    (data['datavaluetype'] == 'Crude Prevalence') &
                    (data['yearstart'] == 2019)
                ]

    return states

def drop_nan_columns(data: pd.DataFrame) -> pd.DataFrame:
    '''drop all NAN rows from our data frame'''
    no_nan = data.dropna()
    return no_nan



