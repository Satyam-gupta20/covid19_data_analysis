# COVID-19 State-Level Data Analysis and Visualization

## Project Overview

This project performs exploratory data analysis (EDA) on a COVID-19 dataset (`COVID19_state.csv`) containing state-level statistics on COVID-19 cases, deaths, testing, and various demographic, economic, and health-related factors. The goal is to uncover patterns, trends, and potential relationships between these factors and the spread/severity of COVID-19 across different U.S. states. All analysis and visualizations are generated programmatically using a Python script, producing static image files.

## Dataset

The dataset used is `COVID19_state.csv`, obtained from Kaggle ([https://www.kaggle.com/datasets/nightranger77/covid19-state-data](https://www.kaggle.com/datasets/nightranger77/covid19-state-data)). It includes the following columns:

-   `State`: Name of the US state
-   `Tested`: Total tests conducted
-   `Infected`: Total confirmed cases
-   `Deaths`: Total deaths
-   `Population`: State population
-   `Pop Density`: Population density
-   `Gini`: Gini coefficient (income inequality)
-   `ICU Beds`: Number of ICU beds
-   `Income`: Median household income
-   `GDP`: Gross Domestic Product
-   `Unemployment`: Unemployment rate
-   `Sex Ratio`: Male to female ratio
-   `Smoking Rate`: Percentage of adult smokers
-   `Flu Deaths`: Historical flu deaths
-   `Respiratory Deaths`: Historical respiratory disease deaths
-   `Physicians`: Number of physicians
-   `Hospitals`: Number of hospitals
-   `Health Spending`: Per capita health spending
-   `Pollution`: Air pollution levels
-   `Med-Large Airports`: Number of medium to large airports
-   `Temperature`: Average temperature
-   `Urban`: Urban population percentage
-   `Age 0-25`, `Age 26-54`, `Age 55+`: Population percentage by age group
-   `School Closure Date`: Date when schools were closed

## Key Features & Techniques

-   **Data Loading and Inspection**: Using Pandas to load CSV data and get initial insights (`.head()`, `.info()`, `.describe()`, `.isnull().sum()`).
-   **Feature Engineering**: Creating new, more insightful metrics from existing data:
    -   `Infection_Rate` (Infected / Population)
    -   `Mortality_Rate` (Deaths / Infected)
    -   `Test_Positivity_Rate` (Infected / Tested)
-   **Exploratory Data Analysis (EDA)**:
    -   Identifying states with the highest/lowest COVID-19 cases, deaths, and calculated rates.
    -   Analyzing the distribution of key COVID-19 metrics.
    -   Investigating correlations between COVID-19 rates and various state-level factors (e.g., population density, income, health infrastructure, demographic factors).
-   **Data Visualization**: Utilizing Matplotlib and Seaborn to create informative plots, which are saved as `.png` image files in the `plots/` directory:
    -   Bar plots for comparing COVID-19 statistics across states.
    -   Heatmaps for visualizing correlations between numerical features.
    -   Scatter plots to explore relationships between two variables (e.g., population density vs. infection rate, smoking rate vs. mortality rate).
    -   Box plots for understanding the distribution of calculated rates.

## How to Run This Project

1.  **Clone the repository (or create the directory and files manually):**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/covid19_data_analysis.git](https://github.com/YOUR_USERNAME/covid19_data_analysis.git)
    cd covid19_data_analysis
    ```
    *Make sure `COVID19_state.csv` is in this directory.*

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    # On macOS/Linux
    source venv/bin/activate
    # On Windows
    .\venv\Scripts\activate
    ```
3.  **Install the required libraries:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Run the Python analysis script:**
    ```bash
    python main.py
    ```
    This will execute the analysis and save all generated plots as `.png` files in the `plots/` directory.

## Technologies Used

-   Python
-   Pandas (for data manipulation and analysis)
-   Matplotlib (for basic plotting and saving figures)
-   Seaborn (for enhanced statistical visualizations)
-   Sublime Text (for coding)

---
