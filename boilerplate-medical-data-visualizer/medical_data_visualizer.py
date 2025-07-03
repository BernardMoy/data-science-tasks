import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv("medical_examination.csv")

# 2
df["overweight"] = ((df["weight"] / (df["height"] * df["height"] / 10000)) > 25).astype(
    int
)

# 3
df["cholesterol"] = (df["cholesterol"] > 1).astype(int)
df["gluc"] = (df["gluc"] > 1).astype(int)


# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(
        df,
        id_vars=["cardio"],  # To keep
        value_vars=[
            "cholesterol",
            "gluc",
            "smoke",
            "alco",
            "active",
            "overweight",
        ],  # To melt
        var_name="variable",  # New name
        value_name="value",  # Values of the value_vars
    )

    # 6
    df_cat = df_cat.groupby(["cardio", "variable", "value"]).size()  # Grouped keys
    df_cat = df_cat.reset_index(name="total")

    # 7
    fig = sns.catplot(
        data=df_cat, x="variable", y="total", col="cardio", hue="value", kind="bar"
    ).fig  # Get the matplotlib fig

    # 8
    # plt.show()

    # 9
    fig.savefig("catplot.png")
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[
        (df["ap_lo"] <= df["ap_hi"])
        & (df["height"] >= df["height"].quantile(0.025))
        & (df["height"] <= df["height"].quantile(0.975))
        & (df["weight"] >= df["weight"].quantile(0.025))
        & (df["weight"] <= df["weight"].quantile(0.975))
    ]

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 14
    fig, ax = plt.subplots()

    # 15
    sns.heatmap(
        corr, mask=mask, cmap="coolwarm", ax=ax, fmt=".1f", annot=True
    )  # Need to annotate the cells on the heatmap
    plt.title("Heat map")
    # plt.show()

    # 16
    fig.savefig("heatmap.png")
    return fig
