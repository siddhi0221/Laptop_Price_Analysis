import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


#load data
df=pd.read_csv("LaptopCD.csv")

# Title and description
st.title("Laptop Analysis Dashboard")
st.markdown("Explore the variation of Price with other columns in the dataset.")
# Sidebar for column selection
categorical_cols = ['Company', 'TypeName', 'Cpu', 'Gpu', 'OpSys']
numerical_cols = ['Ram', 'Weight', 'Touchscreen', 'IPS', 'PPI']

all_columns = categorical_cols + numerical_cols
selected_column = st.sidebar.selectbox("Select a column to compare with Price:", all_columns)

# Plotting
if selected_column:
    if selected_column in categorical_cols:
        # Bar chart for categorical columns
        fig = px.histogram(df, x=selected_column, y="Price", title=f"Price variation by {selected_column}",color_discrete_sequence=px.colors.qualitative.Set2)
    else:
        # Scatter plot for numerical columns
        fig = px.scatter(df, x=selected_column, y="Price", trendline="ols",
                         title=f"Price vs {selected_column}")

    st.plotly_chart(fig)
