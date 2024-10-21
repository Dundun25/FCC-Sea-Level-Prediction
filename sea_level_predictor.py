import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")
    # Create scatter plot
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])
    plt.xlabel('Year')
    plt.ylabel('CSIRO Adjusted Sea Level')
    plt.title('Scatter Plot')
    plt.show()
    # Create first line of best fit
    future_years = list(range(2000, 2051))  # From 2000 to 2050
    future_sea_levels = [slope * year + intercept for year in future_years]
    plt.plot(future_years, future_sea_levels, color='red')  # Line of best fit
    plt.xlabel('Year')
    plt.ylabel('Sea Level (m)')
    plt.title('Sea Level Rise Prediction by 2050')
    
    # Create second line of best fit
    recent_years = [year for year in df["Year"] if year >= 2000]
    recent_sea_levels = [df["CSIRO Adjusted Sea Level"][i] for i, year in enumerate(df["Year"]) if year >= 2000]
    plt.scatter(recent_years, recent_sea_levels, label='Data since 2000')
    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(recent_years, recent_sea_levels)
    future_years_recent = list(range(2000, 2051))
    future_sea_levels_recent = [slope_recent * year + intercept_recent for year in future_years_recent]
    plt.plot(future_years_recent, future_sea_levels_recent, color='blue', label='Best fit since 2000')
    
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    plt.show()
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()