import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title("📊 Sales Dashboard")

# Load data
df = pd.read_csv("sales.csv")

# Show raw data
st.subheader("Raw Data")
st.write(df)

# Basic stats
st.subheader("Basic Analysis")
st.write("Total Sales:", df["Sales"].sum())
st.write("Average Sales:", df["Sales"].mean())
st.write("Max Sales:", df["Sales"].max())

# Grouped data
grouped = df.groupby("Product")["Sales"].sum()

# Bar chart
st.subheader("Sales by Product")
fig1, ax1 = plt.subplots()
grouped.plot(kind='bar', ax=ax1)
st.pyplot(fig1)

# Line chart
st.subheader("Sales Trend")
fig2, ax2 = plt.subplots()
df["Sales"].plot(kind='line', ax=ax2)
st.pyplot(fig2)

# Pie chart
st.subheader("Sales Distribution")
fig3, ax3 = plt.subplots()
grouped.plot(kind='pie', autopct='%1.1f%%', ax=ax3)
ax3.set_ylabel("")
st.pyplot(fig3)

# Filter
st.subheader("High Sales (>150)")
high_sales = df[df["Sales"] > 150]
st.write(high_sales)