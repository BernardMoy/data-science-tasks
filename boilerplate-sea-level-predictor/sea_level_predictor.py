import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np


def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.scatter(
        df["Year"],
        df["CSIRO Adjusted Sea Level"],
    )

    # Create first line of best fit
    slope, intercept, r, p, se = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])

    # Line space is from 1880 to 2050
    x_range = np.arange(1880, 2051)  # One point for each year from 1880 to 2050
    y_range = np.array([slope * i + intercept for i in x_range])

    plt.plot(x_range, y_range, color="blue")

    # Create second line of best fit

    # Filter dataframe to only consider data after year 2000
    df_after_2000 = df.loc[df["Year"] >= 2000]
    slope2, intercept2, r2, p2, se2 = linregress(
        df_after_2000["Year"], df_after_2000["CSIRO Adjusted Sea Level"]
    )

    # Line space is from 2000 to 2050
    x_range2 = np.arange(2000, 2051)
    y_range2 = np.array([slope2 * i + intercept2 for i in x_range2])

    plt.plot(x_range2, y_range2, color="red")

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig("sea_level_plot.png")
    return plt.gca()
