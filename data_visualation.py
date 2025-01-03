import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
columns = ["Name", "Brand channel", "Subscribers (millions)", "Primary language", "Category", "Country"]
data = [
    ["MrBeast", "No", 335, "English", "Entertainment", "United States"],
    ["T-Series", "Yes", 280, "Hindi", "Music", "India"],
    ["Cocomelon - Nursery Rhymes", "Yes", 186, "English", "Education", "United States"],
    ["SET India", "Yes", 180, "Hindi", "Entertainment", "India"],
    ["Vlad and Niki", "No", 129, "English", "Entertainment", "Russia"],
    ["Kids Diana Show", "Yes", 128, "English", "Entertainment", "United States"],
    ["Like Nastya", "No", 123, "English", "Entertainment", "United States"],
    ["Zee Music", "Yes", 112, "Hindi", "Music", "India"],
    ["PewDiePie", "No", 110, "English", "Entertainment", "Sweden"],
    ["WWE", "Yes", 105, "English", "Sports", "United States"],
]
df = pd.DataFrame(data, columns=columns)
print("Data Preview:")
print(df.head())
if df["Subscribers (millions)"].dtype != np.float64:
    df["Subscribers (millions)"] = pd.to_numeric(df["Subscribers (millions)"], errors='coerce')
plt.figure(figsize=(12, 6))
df_sorted = df.sort_values(by="Subscribers (millions)", ascending=False).head(10)
plt.bar(df_sorted["Name"], df_sorted["Subscribers (millions)"], color='skyblue', edgecolor='black')
plt.title("Top 10 YouTube Channels by Subscribers", fontsize=16)
plt.xlabel("Channel Name", fontsize=12)
plt.ylabel("Subscribers (millions)", fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
category_counts = df["Category"].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
plt.title("Distribution of Categories", fontsize=16)
plt.show()
plt.figure(figsize=(12, 6))
unique_countries = df["Country"].unique()
colors = plt.cm.rainbow(np.linspace(0, 1, len(unique_countries)))
for i, country in enumerate(unique_countries):
    country_data = df[df["Country"] == country]
    plt.scatter(
        country_data["Name"],
        country_data["Subscribers (millions)"],
        label=country,
        color=colors[i],
        s=100,
        alpha=0.7
    )
plt.title("Subscribers by Country", fontsize=16)
plt.xlabel("Channel Name", fontsize=12)
plt.ylabel("Subscribers (millions)", fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.legend(title="Country", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()