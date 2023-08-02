import sqlite3
import matplotlib.pyplot as plt
import numpy as np

def generate_plot6():

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
        key = f"{tool}/{run_timeout}"
        
        if key not in data_dict:
            data_dict[key] = []
            labels.append(key)
        
        data_dict[key].append(avg_runtime)

    # Step 3: Create the box plot
    # Create a list to hold all the data arrays for plotting
    data_to_plot = [data_dict[label] for label in labels]

    # Create a unique color map for each tool
    unique_tools = set(tool for _, _, tool in data)
    tool_colors = plt.cm.tab20(np.linspace(0, 1, len(unique_tools)))

    # Map each tool to its respective color
    tool_color_map = {tool: color for tool, color in zip(unique_tools, tool_colors)}

    # Create a figure and axes
    fig, ax = plt.subplots()

    # Create the box plot with custom box colors
    bp = ax.boxplot(data_to_plot, labels=labels, patch_artist=True)

    # Customize each box's color based on the tool
    for box, label in zip(bp['boxes'], labels):
        tool = label.split('/')[0]
        box.set(facecolor=tool_color_map[tool])

    # Optionally, add a title and axis labels
    ax.set_title('Box Plot: Runtime for each tool and run timeout')
    ax.set_xlabel('Tool / Run Timeout')
    ax.set_ylabel('Runtime')

    # Step 4: Change the y-axis to logarithmic scale
    ax.set_yscale('log')

    # Step 5: Create a second Y-axis and copy the tick positions and labels from the original Y-axis
    ax2 = ax.twinx()
    ax2.set_yscale('log')
    ax2.set_ylim(ax.get_ylim())  # Copy the same limits from the original Y-axis

    # Optionally, if you want to customize the appearance of the copied Y-axis tick labels:
    # y_ticks, _ = plt.yticks()
    # ax2.set_yticks(y_ticks)
    # ax2.set_yticklabels([f"{val:.2f}" for val in y_ticks])

    # Rotate the x-axis tick labels vertically
    ax.tick_params(axis='x', rotation=90)

    # Show the plot
    plt.grid(True)
    plt.show()
