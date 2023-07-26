import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the SQLite database
db_path = 'C:/Users/mirha/desktop/plots/sqlite-2023-07-10.db'
conn = sqlite3.connect(db_path)

# SQL query to fetch the desired columns from the table
query = "SELECT run_timeout, result, is_maybe_correct, is_maybe_incorrect FROM _run_group_result WHERE tool='PASDA-diff'AND result IN('MAYBE_EQ', 'MAYBE_NEQ')"

# Use pandas to read the SQL query result into a DataFrame
df = pd.read_sql_query(query, conn)

# Close the database connection
conn.close()

# Group by 'run_timeout' and 'result' and calculate the counts for 'is_maybe_correct' and 'is_maybe_incorrect'
result_counts = df.groupby(['run_timeout', 'result'])[['is_maybe_correct', 'is_maybe_incorrect']].sum()

# Reset the index to make 'run_timeout' and 'result' as columns
result_counts = result_counts.reset_index()

# Rename the columns for clarity
result_counts.rename(columns={'is_maybe_correct': 'Correct', 'is_maybe_incorrect': 'Incorrect'}, inplace=True)

# Pivot the DataFrame to have 'result' as columns and 'run_timeout' as rows
pivot_df = result_counts.pivot(index='run_timeout', columns='result', values=['Correct', 'Incorrect'])

# Flatten the column names after pivoting
pivot_df.columns = [f'{col[0]}_{col[1]}' for col in pivot_df.columns]

# Plot the grouped bar chart for each 'result' category
fig, ax = plt.subplots(figsize=(10, 6))
pivot_df.plot(kind='bar', ax=ax)
ax.grid(True)

# Set plot labels and title
plt.xlabel('Run Timeout')
plt.ylabel('#Counts')
plt.title('Counts of Correct and Incorrect Results for Tool PASDA-Diff for each Run Timeout')

# Create a twin axis on the right side
#ax_right = ax.twinx()

# Plot the values of the right y-axis using the same DataFrame 'pivot_df'
#pivot_df.plot(kind='bar', ax=ax_right, alpha=0)  # Alpha 0 makes the bars invisible

# Set the labels and color of the right y-axis
#ax_right.tick_params(axis='y', colors='black')

# Hide the legend for the right y-axis
#ax_right.get_legend().remove()

# Add the values above each bar
for p in ax.patches:
    height = p.get_height()
    if height > 0:
        ax.annotate(f'{int(height)}', (p.get_x() + p.get_width() / 2., height),
                     xytext=(0, 5),
                    textcoords="offset points", ha='center', va='bottom', rotation='vertical', color='#303030', size='10',fontstyle='italic')

ax.set_ylim(0, 35)


# Show the plot
plt.show()
