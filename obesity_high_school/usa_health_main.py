
'''
    main data module for this package
    a bridge to distribute dataframe to all other modules in this package so we don't
    copy paste sys and os imports again and again 
'''

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

def get_main(data:pd.DataFrame) -> pd.DataFrame:

    return data 

usa_main = get_main(usa_data)