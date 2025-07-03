import matplotlib.pyplot as plt
import pandas as pd
import calendar
import seaborn as sns
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv(
    "fcc-forum-pageviews.csv", index_col="date", parse_dates=True
)  # Parse as dates
print(df.columns)

# Clean data
df = df[
    (df["value"] <= df["value"].quantile(0.975))
    & (df["value"] >= df["value"].quantile(0.025))
]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(df.index, df["value"], color="red")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")

    # Save image and return fig (don't change this part)
    fig.savefig("line_plot.png")
    return fig


def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar["Year"] = df.index.year
    df_bar["Months"] = df.index.month
    df_bar = df_bar.groupby(["Year", "Months"])

    df_grouped = df_bar["value"].mean().reset_index(name="avg")

    pivoted_df = df_grouped.pivot(columns="Months", values="avg", index="Year").fillna(
        0
    )

    # Rename the columns for 1 to jan, 2 to feb...
    pivoted_df.rename(
        columns={
            1: "January",
            2: "February",
            3: "March",
            4: "April",
            5: "May",
            6: "June",
            7: "July",
            8: "August",
            9: "September",
            10: "October",
            11: "November",
            12: "December",
        },
        inplace=True,
    )

    # print(pivoted_df.head())

    # Draw bar plot
    fig, ax = plt.subplots(figsize=(12, 6))
    pivoted_df.plot(kind="bar", stacked=False, ax=ax)
    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")

    # Save image and return fig (don't change this part)
    fig.savefig("bar_plot.png")
    return fig


def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box["year"] = [d.year for d in df_box.date]
    df_box["month"] = [d.strftime("%b") for d in df_box.date]

    # Draw box plots (using Seaborn)

    # Save image and return fig (don't change this part)
    fig.savefig("box_plot.png")
    return fig
