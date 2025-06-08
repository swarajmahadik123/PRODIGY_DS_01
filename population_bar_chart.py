import pandas as pd
import matplotlib.pyplot as plt

# Read data (replace with your actual path)
df = pd.read_csv("API_SP.POP.TOTL_DS2_en_csv_v2_2590.csv", skiprows=4)

# Preview data
print(df[['Country Name', '2022']].head())

# Select top 10 countries by 2022 population
top_countries = df[['Country Name', '2022']].dropna().sort_values('2022', ascending=False).head(10)

# Plot
plt.figure(figsize=(10,6))
plt.bar(top_countries['Country Name'], top_countries['2022'], color='skyblue')
plt.title('Top 10 Countries by Population (2022)', fontsize=14)
plt.xticks(rotation=45, ha='right')
plt.ylabel('Population')
plt.tight_layout()
plt.show()
