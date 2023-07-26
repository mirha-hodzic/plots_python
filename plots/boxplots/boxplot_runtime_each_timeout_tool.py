import sqlite3
import matplotlib.pyplot as plt
import numpy as np

# Step 1: Connect to the SQLite database and retrieve the data
db_path = "C:/Users/mirha/Desktop/plots/sqlite-2023-07-10.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Execute the query to retrieve the data
query = "SELECT avg_runtime, run_timeout, tool FROM _run_group;"
cursor.execute(query)
data = cursor.fetchall()

# Close the connection to the database
conn.close()

# Step 2: Process the data for plotting
data_dict = {}
labels = []

for avg_runtime, run_timeout, tool in data:
    key = f"{run_timeout}/{tool}"
    
    if key not in data_dict:
        data_dict[key] = []
        labels.append(key)
    
    data_dict[key].append(avg_runtime)

# Step 3: Sort the labels based on run_timeout (numerically)
sorted_labels = sorted(labels, key=lambda x: int(x.split('/')[0]))

# Step 4: Create the box plot
# Create a list to hold all the data arrays for plotting
data_to_plot = [data_dict[label] for label in sorted_labels]

# Create a unique color map for each run timeout using a suitable colormap
unique_timeouts = sorted(set(int(label.split('/')[0]) for label in sorted_labels))
timeout_colors = plt.cm.tab20(np.linspace(0, 1, len(unique_timeouts)))

# Map each timeout to its respective color
timeout_color_map = {timeout: color for timeout, color in zip(unique_timeouts, timeout_colors)}

# Create a figure and axes
fig, ax = plt.subplots()

# Create the box plot with custom box colors
bp = ax.boxplot(data_to_plot, labels=sorted_labels, patch_artist=True)

# Customize each box's color based on the run timeout
for box, label in zip(bp['boxes'], sorted_labels):
    timeout = int(label.split('/')[0])  # Get the run timeout from the label
    box.set(facecolor=timeout_color_map[timeout])

# Optionally, add a title and axis labels
ax.set_title('Box Plot: Runtime for each run timeout and tool')
ax.set_xlabel('Run Timeout / Tool')
ax.set_ylabel('Runtime')

# Step 5: Change the y-axis to logarithmic scale
ax.set_yscale('log')

ax2 = ax.twinx()
ax2.set_yscale('log')
ax2.set_ylim(ax.get_ylim())

# Show the plot
ax.tick_params(axis='x', rotation=90)
plt.tight_layout()
plt.grid(True)
plt.show()
