
import matplotlib.pyplot as plt 

def display_top_states_comparison() -> None:

    '''
        showing only 10 states so decided to create a simple dictionary instead 
        importing pandas dataframes from hs_overweight_or_obesity.py and sorting values from 2013 & 2019
        dictionary is for display purpose only
    '''
    states = {
        'AR' : [36.3, 41.9], 
        'MS' : [37.5, 41.4], 
        'WV' : [35.5, 39.4], 
        'TN' : [32.3, 39.2], 
        'AL' : [37.9, 37.4],
        'GA' : [36.6, 36.4], 
        'KY' : [31.5, 36.2], 
        'OK' : [44.5, 35.7], 
        'DC' : [36.0, 34.7], 
        'TX' : [38.3, 34.7]
    }

    # put state values in a list
    values = [
                36.3, 41.9, 37.5, 41.4, 35.5, 39.4,
                32.3, 39.2, 37.9, 37.4, 36.6, 36.4,
                31.5, 36.2, 44.5, 35.7, 36.0, 34.7,
                38.3, 34.7
            ]

    # put assignment numbers to stems
    stems = [
                1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 
                6, 6, 7, 7, 8, 8, 9, 9, 10, 10
            ]

    # get necessary colors
    bg_color = '#111a12'
    orange = '#fc9673'
    white = '#FFF3E2'

    #create stem chart base
    fig, ax = plt.subplots()
    marker, line, base = ax.stem(stems, values, basefmt=' ', orientation='horizontal')

    #modify chart base
    fig.patch.set_facecolor(bg_color)
    ax.set_facecolor(bg_color)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)

    plt.setp(line, linewidth=5, color=orange)
    plt.setp(marker, markersize=20, color=orange)

    plt.xticks(color = white)
    plt.yticks(color = white)

    plt.xlim([30, 47])
    plt.ylim([0, 11])

    plt.show()

display_top_states_comparison()   