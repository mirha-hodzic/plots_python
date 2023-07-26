import sqlite3
import matplotlib.pyplot as plt
import numpy as np

# Connect to the SQLite database
conn = sqlite3.connect('C:/Users/mirha/Desktop/plots/sqlite-2023-07-10.db')
cursor = conn.cursor()

# Fetch the data from the database
cursor.execute("SELECT tool, run_timeout, avg_runtime FROM _run_group_result_list")
data = cursor.fetchall()

# Close the connection
conn.close()

# Create a dictionary to group avg_runtimes by tool and run_timeout
tool_run_times = {}
for row in data:
    tool, run_timeout, avg_runtime = row
    if tool not in tool_run_times:
        tool_run_times[tool] = {}
    tool_run_times[tool][run_timeout] = avg_runtime

# Get unique tools and run_timeouts
unique_tools = list(tool_run_times.keys())
unique_run_timeouts = sorted(set(run_timeout for run_times in tool_run_times.values() for run_timeout in run_times))

# Set up the figure and axes
fig, ax = plt.subplots()
ax2 = ax.twinx()  # Create a secondary y-axis on the right side
bar_width = 0.2

# Create positions for bars
bar_positions = np.arange(len(unique_run_timeouts)) * 1.5

# Plot each tool's bars for each run_timeout
for i, tool in enumerate(unique_tools):
    run_timeout_values = [tool_run_times[tool].get(run_timeout, 0) for run_timeout in unique_run_timeouts]

    offset = bar_width * i

    rects = ax.bar(bar_positions + offset, run_timeout_values, width=bar_width, label=f"Tool: {tool}")

    # Add labels above non-zero bars (rounded to integers) with increased spacing
    for rect, value in zip(rects, run_timeout_values):
        if value != 0:
            height = rect.get_height()
            ax.annotate(f"{int(value)}", xy=(rect.get_x() + rect.get_width() / 2, height), xytext=(0, 3),
                        textcoords="offset points", ha='center', va='bottom', rotation='vertical', color='#303030', size='10',fontstyle='italic')

# Set the x-axis and y-axis labels
ax.set_xticks(bar_positions + (len(unique_tools) - 1) * bar_width / 2)
ax.set_xticklabels(unique_run_timeouts)
ax.set_xlabel('Run Timeout')
ax.set_ylabel('Runtime')

# Set the y-axis limits and ticks for the primary y-axis (left side)
left_yticks = np.linspace(0, 1100, 12)  # 12 ticks from 0 to 1100 (evenly distributed)
ax.set_yticks(left_yticks)
ax.set_ylim(0, 1100)  # Set the y-axis limit to 0 and 1100

# Set the y-axis limits and ticks for the secondary y-axis (right side)
right_yticks = np.linspace(0, 1100, 12)  # 12 ticks from 0 to 1100 (evenly distributed)
ax2.set_yticks(right_yticks)
ax2.set_ylim(0, 1100)  # Set the y-axis limit to 0 and 1100
right_yticklabels = [f"{int(y)}" for y in right_yticks]
right_max_length = max(len(label) for label in right_yticklabels)  # Find the maximum length of right y-axis labels
right_yticklabels = [label.rjust(right_max_length) for label in right_yticklabels]  # Right-align the labels
ax2.set_yticklabels(right_yticklabels)

# Add a legend
ax.legend(facecolor='lightgrey')

# Show the plot
plt.title("Grouped bar plot - Runtime sorted by runtimeout")
plt.tight_layout()
plt.grid(True)
plt.show()
