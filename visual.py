import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Streamlit Title
st.title("YouTube Channel Analysis")

# Load data from CSV file
data_file = "youtube_data.csv"
df = pd.read_csv(data_file)

# Convert subscribers column to numeric (if not already numeric)
df["Subscribers (millions)"] = pd.to_numeric(df["Subscribers (millions)"], errors="coerce")

# Display dataset preview
st.subheader("Dataset Preview")
st.dataframe(df)

# Top 10 YouTube Channels by Subscribers
st.subheader("Top 10 YouTube Channels by Subscribers")
df_sorted = df.sort_values(by="Subscribers (millions)", ascending=False).head(10)
st.bar_chart(data=df_sorted.set_index("Name")["Subscribers (millions)"])

# Distribution of Categories
st.subheader("Distribution of Categories")
category_counts = df["Category"].value_counts()

fig, ax = plt.subplots()
colors = plt.cm.Paired(np.arange(len(category_counts)))
ax.pie(category_counts, labels=category_counts.index, autopct="%1.1f%%", startangle=140, colors=colors)
ax.set_title("Category Distribution")
st.pyplot(fig)

# Subscribers by Country
st.subheader("Subscribers by Country")
unique_countries = df["Country"].unique()
colors = plt.cm.rainbow(np.linspace(0, 1, len(unique_countries)))

fig, ax = plt.subplots(figsize=(12, 6))
for i, country in enumerate(unique_countries):
    country_data = df[df["Country"] == country]
    ax.scatter(
        country_data["Name"],
        country_data["Subscribers (millions)"],
        label=country,
        color=colors[i],
        s=100,
        alpha=0.7,
    )
ax.set_title("Subscribers by Country")
ax.set_xlabel("Channel Name")
ax.set_ylabel("Subscribers (millions)")
ax.legend(title="Country", bbox_to_anchor=(1.05, 1), loc="upper left")
ax.tick_params(axis="x", rotation=45)
st.pyplot(fig)

# Add snow effect
st.snow()
