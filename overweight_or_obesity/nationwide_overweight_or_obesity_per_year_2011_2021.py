
import pandas as pd
from overweight_or_obesity_nationwide import nationwide_overweight_or_obesity 

def get_nationwide_obesity_per_year(ob: pd.DataFrame) -> dict[int:float]:

    values = {}
    for i in ob.index:
        year = ob.loc[i, 'yearstart']
        value = ob.loc[i, 'datavaluealt']
        values[year] = value

    return values

def sort_nationwide_values(nwide: dict[int:float]) -> list[tuple]:

    return sorted(nwide.items(), key = lambda x: x[0], reverse=True)

nwide = get_nationwide_obesity_per_year(nationwide_overweight_or_obesity)
nationwide_per_year = sort_nationwide_values(nwide) 

