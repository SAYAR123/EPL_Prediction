import streamlit as st
import pandas as pd

from paths import EPL_CSV

from ui import hero, dataset_source_badge

@st.cache_resource
def db():
    # df=pd.read_csv(r"C:\Projects\football_final\data\epl_final.csv")
    df=pd.read_csv(EPL_CSV)
    return df

df=db()

# Reset index to make it a data column named "index"
df_reset = df.reset_index()

# Shift just that column's values by 1
df_reset["index"] = df_reset["index"] + 1

def data_set(): 

    hero(
        "Training Dataset",
        "English Premier League match data(2000-2025) used for training and evaluating all prediction models."
    )

    dataset_source_badge(
        label="Kaggle - English Premier League (EPL) Match Data 2000-2025",
        url="https://www.kaggle.com/datasets/marcohuiii/english-premier-league-epl-match-data-2000-2025"
    )

    st.write('---')

    # Hide the automatic 0-based index and rename the new column
    st.dataframe(
        df_reset,
        column_config={"index": "SL. No."},
        hide_index=True
    )