# ---WEBAPP---
import pandas as pd
import plotly.express as px
import streamlit as st
import altair as alt
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(
    page_title="DataQuest 2023",
    page_icon=":bar_chart:",
    layout="centered"
)

# read data
dfcsv = pd.read_csv("train_data.csv")


# ==================================
# DASHBOARD
st.title(":bar_chart: Hotel Cancellation")
st.markdown("##")
# Metrics
# Row 
st.markdown('### Hotel Cancellation')


# ==================================
# FILTER
st.sidebar.header("Please Filter Here:")

mealplan = st.sidebar.multiselect(
    "Select the Username:",
    options=dfcsv["MealPlan"].unique(),
    default=dfcsv["MealPlan"].unique()
)

df_selection = dfcsv.query(
    "MealPlan == @mealplan"
)


# ==================================
# DATA VISUALIZATION
# --static--
# CHART 1
st.header("Stacked Bar")
# bar_chart = alt.Chart(df).mark_bar().encode(
#     x = 'username',
#     y= {'rm', 'g', 'd', 'c', 'tv', 'pc', 'car', 'w', 'pt'},
#     color = 'username'
# )
# st.altair_chart(bar_chart, use_container_width=True)

# fig, ax = plt.subplots()
# dfcsv.plot.bar(x='username',
#     y = ['Red Meat', 'Grains', 'Dairy', 'Cellphone', 'TV', 'Computer', 'Car', 'Walking', 'Public Transport'],
#     stacked = True,
#     ax=ax
# )
# st.pyplot(fig)

# --dynamic--
# CHART 2


# ==================================
# RAW TABLE
st.header("Scraped Data")
st.dataframe(df_selection)