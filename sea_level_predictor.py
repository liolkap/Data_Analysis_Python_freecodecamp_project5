import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    df.fillna(0, inplace=True)

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(8, 7))
    ax.scatter(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])
    ax.grid(True)

    # Create first line of best fit
    plot_years1 = range(1880, 2051)
    l1 = linregress(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])
    ax.plot(plot_years1, (l1.intercept + l1.slope * plot_years1), color='purple')

    # Create second line of best fit
    plot_years2 = range(2000, 2051)
    l2 = linregress(x=range(2000, 2014), y=df['CSIRO Adjusted Sea Level'].loc[df['Year'] >= 2000])
    ax.plot(plot_years2, (l2.intercept + l2.slope * plot_years2), color='red')

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
