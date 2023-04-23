
import matplotlib.pyplot as plt 
import sys, os 

userprofile = os.getenv('USERPROFILE')
file_path = f'{userprofile}\Desktop\github\\us_high_school_overweight_obesity\overweight_or_obesity'
sys.path.append(file_path)

from nationwide_overweight_or_obesity_per_year_2011_2021 import nationwide_per_year

def display_nationwide_obesity_2011_2021(npy: list[tuple]) -> None:

    year = [x[0] for x in npy]
    values = [x[1] for x in npy]

    bg_color = '#111a12'
    orange = '#fc9673'
    dark_orange = '#784938'
    white = '#FFF3E2'
    
    fig, ax = plt.subplots()
    plt.plot(
        year, 
        values, 
        marker='o',
        linestyle = 'solid',
        color = orange
    )

    fig.patch.set_facecolor(bg_color)
    ax.set_facecolor(bg_color)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color(dark_orange)
    ax.spines['bottom'].set_color(dark_orange)

    plt.suptitle(
        'USA OVERWEIGHT OR OBESITY RATES AMONG ADULTS >= 18 YEARS OLD',
        fontfamily = 'Microsoft New Tai Lue',
        fontsize = 18,
        fontweight = 'bold',
        color = orange
    )

    plt.title(
        '*source https://catalog.data.gov/dataset/u-s-chronic-disease-indicators-cdi',
        fontfamily = 'Microsoft New Tai Lue',
        color = dark_orange
    )

    plt.ylabel(
        'PERCENTAGE',
        fontfamily = 'Microsoft New Tai Lue',
        fontsize = 12.5,
        color = dark_orange
    )

    plt.xlabel(
        'YEAR',
        fontfamily = 'Microsoft New Tai Lue',
        fontsize = 12.5,
        color = dark_orange
    )

    plt.xticks(color = orange)
    plt.yticks(color = orange)

    values.reverse()
    for index, value in enumerate(values):
        plt.text(
            index, 
            value, 
            f'{str(value)}%',
            position = (index+2010.50, value+0.1),
            color = white,
            fontweight = 'bold',
            fontsize = 15
        )

    plt.show()

display_nationwide_obesity_2011_2021(nationwide_per_year)