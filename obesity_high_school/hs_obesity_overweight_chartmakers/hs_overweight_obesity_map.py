

import sys, os  
import pandas as pd 
import plotly.express as px 

userprofile = os.getenv('USERPROFILE')
file_path = f'{userprofile}\Desktop\github\\us_high_school_overweight_obesity\obesity_high_school'
sys.path.append(file_path)

from hs_overweight_or_obesity_states_2019 import oob_sto_2019 

def display_hs_overweight_obesity_map(oob:pd.DataFrame) -> None:

    fig = px.choropleth(
                        oob, 
                        locations='locationabbr',
                        locationmode='USA-states',
                        scope='usa',
                        color='datavaluealt',
                        range_color=[20,50],
                        color_continuous_scale=['#F9D949', '#fc9673', '#fe4704']
          ).update_layout(
                        template='none',
                        plot_bgcolor='#111a12',
                        paper_bgcolor = '#111a12'
          )

    fig.show()

display_hs_overweight_obesity_map(oob_sto_2019)

