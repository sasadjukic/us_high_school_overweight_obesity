
import pandas as pd 
import sys, os

'''
    find datasheet on the hard disk,
    add it's path to the list of paths,
    import it 
'''

userprofile = os.getenv('USERPROFILE')
file_path = f'{userprofile}\Desktop\github\\us_high_school_overweight_obesity\main_data'
sys.path.append(file_path)

from data import usa_data

def get_overweight_or_obesity_main(data: pd.DataFrame) -> pd.DataFrame:

    ooo_main = data[data['question'] == 'Overweight or obesity among adults aged >= 18 years']
    return ooo_main

def get_overweight_or_obesity_value_columns(main: pd.DataFrame) -> pd.DataFrame:

    overweight_or_obesity = main[['yearstart', 'locationabbr', 'datavaluealt',  'stratification1', 'datavaluetype']]
    return overweight_or_obesity

def get_nationwide_overweight_or_obesity_crude_values(ob: pd.DataFrame) -> pd.DataFrame:

    nationwide = ob[(ob['stratification1'] == 'Overall') & 
                    (ob['datavaluetype'] == 'Crude Prevalence') & 
                    (ob['locationabbr'] == 'US')
                   ]

    return nationwide

overweight_or_obesity_main = get_overweight_or_obesity_main(usa_data)
overweight_or_obesity = get_overweight_or_obesity_value_columns(overweight_or_obesity_main)
nationwide_overweight_or_obesity = get_nationwide_overweight_or_obesity_crude_values(overweight_or_obesity)






