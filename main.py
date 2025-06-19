import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
import os 

plt.style.use('seaborn-v0_8-darkgrid')

#create a directory for saving plots if it doesn't exist
plots_dir = 'plots'
if not os.path.exists(plots_dir):
	os.makedirs(plots_dir)
	print("created a new folder: ", plots_dir)

# 1. Load the dataset
try:
	df = pd.read_csv('COVID19_state.csv')
	print("Datset Loaded successfully")
except Exception as e:
	print("Error: ", e)
	exit() #exit if data is not loaded.

# 2. Initial Dataset exploration
print('---Head of the Dataset---')
print(df.head())

print('---dataset info---')
print(df.info())

print('---Descriptive statistics---')
print(df.describe())

print('---missing values count---')
print(df.isnull().sum())

# 3. Data Cleaning and Feature Engineering

# Create new insightful metrics
# To avoid division by zero errors, let's add a small epsilon or check for zero values
epsilon = 1e-6 # A small number to prevent division by zero

df['Infection_Rate'] = (df['Infected'] / (df['Population'] + epsilon)) *100
df['Mortality_Rate'] = (df['Deaths'] / (df['Infected'] + epsilon)) *100
df['Test_Positivity_Rate'] = (df['Infected'] / (df['Tested'] + epsilon)) *100

#dataframe with new features:
print(df[['State', 'Infected', 'Deaths', 'Tested', 'Population', 'Infection_Rate', 'Mortality_Rate', 'Test_Positivity_Rate']].head())

# 4. Exploratory Data Analysis and Visualization 

# sort by infected for consistent visualization
df_sorted_infected = df.sort_values(by = 'Infected', ascending=False)

# Plot: top 10 states by infected cases
plt.figure(figsize=(14, 8))
sns.barplot(x='State', y='Infected', data=df_sorted_infected.head(10), palette='viridis')
plt.title('Top 10 States by Total Infected Cases')
plt.xlabel('State')
plt.ylabel('Total Infected Cases')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig(os.path.join(plots_dir, 'top_10_infected_states.png'))
plt.close() # Close the plot to free memory

# Plot: Top 10 States by Deaths
plt.figure(figsize=(14, 8))
sns.barplot(x='State', y='Deaths', data=df_sorted_infected.head(10), palette='magma') # Using same sort for comparison
plt.title('Top 10 States by Total Deaths')
plt.xlabel('State')
plt.ylabel('Total Deaths')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig(os.path.join(plots_dir, 'top_10_death_states.png'))
plt.close()

# Plot: Top 10 States by Infection Rate
df_sorted_infection_rate = df.sort_values(by='Infection_Rate', ascending=False)
plt.figure(figsize=(14, 8))
sns.barplot(x='State', y='Infection_Rate', data=df_sorted_infection_rate.head(10), palette='plasma')
plt.title('Top 10 States by Infection Rate (%)')
plt.xlabel('State')
plt.ylabel('Infection Rate (%)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig(os.path.join(plots_dir, 'top_10_infection_rate_states.png'))
plt.close()

# Plot: Top 10 States by Mortality Rate
df_sorted_mortality_rate = df.sort_values(by='Mortality_Rate', ascending=False)
plt.figure(figsize=(14, 8))
sns.barplot(x='State', y='Mortality_Rate', data=df_sorted_mortality_rate.head(10), palette='cividis')
plt.title('Top 10 States by Mortality Rate (%)')
plt.xlabel('State')
plt.ylabel('Mortality Rate (%)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig(os.path.join(plots_dir, 'top_10_mortality_rate_states.png'))
plt.close()

# Correlation Matrix of COVID-19 Metrics and other factors
# Select relevant numerical columns for correlation analysis
numeric_cols = ['Tested', 'Infected', 'Deaths', 'Population', 'Pop Density', 'Gini', 'ICU Beds',
                'Income', 'GDP', 'Unemployment', 'Sex Ratio', 'Smoking Rate', 'Flu Deaths',
                'Respiratory Deaths', 'Physicians', 'Hospitals', 'Health Spending', 'Pollution',
                'Med-Large Airports', 'Temperature', 'Urban', 'Age 0-25', 'Age 26-54', 'Age 55+',
                'Infection_Rate', 'Mortality_Rate', 'Test_Positivity_Rate']

plt.figure(figsize=(18, 15))
sns.heatmap(df[numeric_cols].corr(), annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
plt.title('Correlation Matrix of COVID-19 Metrics and State Factors')
plt.xticks(rotation=90)
plt.yticks(rotation=0)
plt.tight_layout()
plt.savefig(os.path.join(plots_dir, 'correlation_matrix.png'))
plt.close()

# Scatter plot: Population Density vs. Infection Rate
plt.figure(figsize=(10, 7))
sns.scatterplot(x='Pop Density', y='Infection_Rate', hue='State', data=df, s=100, alpha=0.7)
plt.title('Population Density vs. Infection Rate')
plt.xlabel('Population Density')
plt.ylabel('Infection Rate (%)')
plt.xscale('log') # Use log scale for population density as it varies widely
plt.grid(True, which="both", ls="-", c=".7")
plt.tight_layout()
plt.savefig(os.path.join(plots_dir, 'pop_density_vs_infection_rate.png'))
plt.close()

# Scatter plot: Smoking Rate vs. Mortality Rate
plt.figure(figsize=(10, 7))
sns.scatterplot(x='Smoking Rate', y='Mortality_Rate', hue='State', data=df, s=100, alpha=0.7)
plt.title('Smoking Rate vs. Mortality Rate')
plt.xlabel('Smoking Rate (%)')
plt.ylabel('Mortality Rate (%)')
plt.tight_layout()
plt.savefig(os.path.join(plots_dir, 'smoking_rate_vs_mortality_rate.png'))
plt.close()

# Box plot: Distribution of key rates
plt.figure(figsize=(15, 6))
sns.boxplot(data=df[['Infection_Rate', 'Mortality_Rate', 'Test_Positivity_Rate']])
plt.title('Distribution of COVID-19 Rates Across States')
plt.ylabel('Percentage (%)')
plt.tight_layout()
plt.savefig(os.path.join(plots_dir, 'rates_distribution_boxplot.png'))
plt.close()

print(f"\nAnalysis complete. All plots saved to the '{plots_dir}' directory.")


















































































