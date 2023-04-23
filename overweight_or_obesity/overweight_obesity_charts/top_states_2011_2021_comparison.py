
import matplotlib.pyplot as plt

def display_states_comparisons_2011_2021() -> None:

    states = {
        'AL' : [66.7, 71.8],
        'AR' : [64.9, 70.4],
        'IA' : [64.8, 70.7],
        'KS' : [64.4, 70.5],
        'KY' : [66.5, 72.3],
        'LA' : [67.6, 71.0],
        'MS' : [68.9, 72.7],
        'ND' : [63.8, 70.1],
        'NE' : [64.9, 71.0],
        'OH' : [65.9, 71.1],
        'OK' : [65.4, 71.9],
        'SC' : [65.9, 70.5],
        'SD' : [64.4, 72.2],
        'TN' : [66.5, 71.6],
        'WV' : [68.9, 73.5]
    }

    values = [
                66.7, 71.8, 64.9, 70.4, 64.8, 70.7,
                64.4, 70.5, 66.5, 72.3, 67.6, 71.0,
                68.9, 72.7, 63.8, 70.1, 64.9, 71.0,
                65.9, 71.1, 65.4, 71.9, 65.9, 70.5,
                64.4, 72.2, 66.5, 71.6, 68.9, 73.5
            ]

    stems = [
                1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6,
                7, 7, 8, 8, 9, 9, 10, 10, 11, 11,
                12, 12, 13, 13, 14, 14, 15, 15
            ]

    bg_color = '#111a12'
    orange = '#fc9673'
    dark_orange = '#784938'
    white = '#FFF3E2'

    fig, ax = plt.subplots()
    marker, line, base = ax.stem(stems, values, basefmt=' ', orientation='horizontal')

    fig.patch.set_facecolor(bg_color)
    ax.set_facecolor(bg_color)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)

    plt.setp(line, linewidth=5, color=orange)
    plt.setp(marker, markersize=20, color=orange)

    plt.xticks(color = dark_orange)
    plt.yticks(color = dark_orange)

    plt.xlim([61, 75])
    plt.ylim([0, 16])
    plt.show()

display_states_comparisons_2011_2021()