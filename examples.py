import pandas as pd
import numpy as np
import forgekit as fk  # Import the forgekit module directly for more DRY code

# STEP 1: Loading and displaying initial data
print("Step 1: Loading and displaying the initial data.")
df1 = pd.DataFrame({
    'A': np.random.randint(1, 100, 50),
    'B': np.random.normal(0, 1, 50),
    'C': np.random.choice(['red', 'blue', 'green'], 50),
    'D': np.random.randint(1, 1000, 50)
})
fk.display_dataframe(df1)  # Directly call the method from forgekit
input("Press Enter to continue...")

# STEP 2: Summary statistics
print("Step 2: Generating summary statistics for numerical columns.")
fk.summary_stats(df1)
input("Press Enter to continue...")

# STEP 3: Normalizing data (min-max scaling)
print("Step 3: Normalizing numerical columns 'A' and 'B'.")
normalized_df = fk.minmax_scale(df1[['A', 'B']])
fk.display_dataframe(normalized_df)
input("Press Enter to continue...")

# STEP 4: Plotting data
print("Step 4: Plotting a line chart for normalized columns 'A' and 'B'.")
fk.plot_dataframe(normalized_df, kind='line', title="Normalized Data Plot")
input("Press Enter to continue...")

# STEP 5: Handling missing data by introducing NaN values and imputing them
print("Step 5: Introducing missing data and imputing with mean for numerical columns.")
df_with_nan = df1.copy()
df_with_nan.loc[0:5, 'A'] = np.nan  # Introduce missing values

# Impute missing values only in numeric columns
numeric_columns = df_with_nan.select_dtypes(include=[np.number]).columns
df_with_nan[numeric_columns] = fk.impute_missing_data(df_with_nan[numeric_columns], strategy='mean')
fk.display_dataframe(df_with_nan)
input("Press Enter to continue...")

# STEP 6: Removing outliers
print("Step 6: Removing outliers from columns 'A' and 'B'.")
df_cleaned = fk.remove_outliers(df1, columns=['A', 'B'])
fk.display_dataframe(df_cleaned)
input("Press Enter to continue...")

# STEP 7: K-means clustering
print("Step 7: Performing K-means clustering with 3 clusters.")
df_clustered = fk.kmeans_clustering(df1[['A', 'B']], n_clusters=3)
fk.display_dataframe(df_clustered)
input("Press Enter to continue...")

# STEP 8: Generating a rolling average plot for column 'A'
print("Step 8: Generating a rolling average (window=5) for column 'A'.")
rolling_avg_df = fk.rolling_average(df1, column='A', window=5)
fk.plot_dataframe(rolling_avg_df, kind='line', title="Rolling Average of A")
input("Press Enter to continue...")

# STEP 9: Generating a custom interactive plot using Plotly
print("Step 9: Creating an interactive scatter plot between 'A' and 'B'.")
fk.interactive_plot(df1, x_col='A', y_col='B', kind='scatter', title="Interactive Scatter Plot")
input("Press Enter to continue...")

# STEP 10: Generating a markdown report of the DataFrame
print("Step 10: Generating a markdown report of the DataFrame.")
fk.generate_report(df1, file_name='data_report.md')
input("Press Enter to continue...")

# BONUS STEP: One-hot encoding of categorical data
print("Bonus Step: One-hot encoding of the 'C' column.")
df_encoded = fk.one_hot_encode(df1, columns=['C'])
fk.display_dataframe(df_encoded)
input("Press Enter to continue...")

# BONUS STEP: Log transformation of 'A' and 'D' columns
print("Bonus Step: Applying log transformation to columns 'A' and 'D'.")
df_log_transformed = fk.log_transform(df1, columns=['A', 'D'])
fk.display_dataframe(df_log_transformed)
input("Press Enter to finish!")
