# Import required libraries
import os
import pandas as pd
import matplotlib.pyplot as plt

# Set working directory (UPDATE THIS TO YOUR OWN FOLDER PATH)
working_directory = "/IBI/IBI1_2025-26-master/Practical10"
os.chdir(working_directory)

# Check working directory
print("Current working directory:", os.getcwd())
print("Files in directory:", os.listdir())

# Load dataset
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")
print("\nData loaded successfully!")

# --------------------------
# Data exploration
# --------------------------
print("\n=== First 5 rows ===")
print(dalys_data.head())

print("\n=== Data information ===")
dalys_data.info()

print("\n=== Statistical summary ===")
print(dalys_data.describe())

# Basic statistics
max_dalys = dalys_data['DALYs'].max()
min_dalys = dalys_data['DALYs'].min()
min_year = dalys_data['Year'].min()
max_year = dalys_data['Year'].max()

print(f"\nMaximum DALYs: {max_dalys}")
print(f"Minimum DALYs: {min_dalys}")
print(f"Earliest year: {min_year}")
print(f"Latest year: {max_year}")

# --------------------------
# Task 1: First 10 rows (Afghanistan)
# --------------------------
afghanistan_first_10 = dalys_data.iloc[0:10, [2, 3]]
print("\n=== Afghanistan first 10 years ===")
print(afghanistan_first_10)

max_val_afg = afghanistan_first_10['DALYs'].max()
year_max_afg = afghanistan_first_10.loc[afghanistan_first_10['DALYs'] == max_val_afg, 'Year'].values[0]
print(f"\nYear with highest DALYs in first 10 years: {year_max_afg}")

# --------------------------
# Task 2: Zimbabwe data
# --------------------------
zimbabwe_data = dalys_data.loc[dalys_data['Entity'] == 'Zimbabwe']
print("\n=== Zimbabwe data ===")
print(zimbabwe_data)

first_zim = zimbabwe_data['Year'].min()
last_zim = zimbabwe_data['Year'].max()
print(f"\nZimbabwe data ranges from {first_zim} to {last_zim}")

# --------------------------
# Task 3: Highest and lowest in 2019
# --------------------------
data_2019 = dalys_data.loc[dalys_data['Year'] == 2019, ['Entity', 'DALYs']]

max_row = data_2019.loc[data_2019['DALYs'] == data_2019['DALYs'].max()]
min_row = data_2019.loc[data_2019['DALYs'] == data_2019['DALYs'].min()]

country_max = max_row['Entity'].values[0]
country_min = min_row['Entity'].values[0]

val_max = max_row['DALYs'].values[0]
val_min = min_row['DALYs'].values[0]

print(f"\nIn 2019:")
print(f"Highest DALYs: {country_max} ({val_max})")
print(f"Lowest DALYs: {country_min} ({val_min})")

# --------------------------
# Task 4: Plot DALYs trend (LINE CHART ONLY)
# --------------------------
selected_country = country_max
country_data = dalys_data.loc[dalys_data['Entity'] == selected_country, ['Year', 'DALYs']]

plt.figure(figsize=(12, 6))
plt.plot(country_data['Year'], country_data['DALYs'], color='#2c3e50', marker='+', linewidth=2, markersize=8, label=selected_country)

plt.title(f'Trend of DALYs Rate Over Time in {selected_country} (1990–2020)', fontsize=14, pad=15)
plt.xlabel('Year', fontsize=12)
plt.ylabel('DALYs Rate (per 100,000 people)', fontsize=12)

plt.grid(True, alpha=0.3)
plt.xticks(rotation=45)
plt.legend(fontsize=11)
plt.tight_layout()
plt.savefig(f'{selected_country}_DALYs_trend.png', dpi=300, bbox_inches='tight')
plt.show()