import sqlite3
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

def generate_plot11():
    # Connect to the SQLite database
    db_path = "C:/Users/mirha/Desktop/plots/sqlite-2023-07-10.db"
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    # Query the data from the "_run_group" table for different run_timeout values
    run_timeouts = [10, 30, 90, 300, 900, 3600]
    data_sets = {}

    for run_timeout in run_timeouts:
        query = f"SELECT avg_result_runtime FROM _run_group WHERE all_correct=1 AND tool='PASDA-diff' AND run_timeout={run_timeout} ORDER BY avg_result_runtime ASC"
        cursor.execute(query)
        data_sets[run_timeout] = cursor.fetchall()

    # Close the database connection
    connection.close()

    # Create x and y values for each data set and plot them separately
    fig, ax = plt.subplots()

    for run_timeout, data in data_sets.items():
        x_values = [row[0] for row in data]
        y_values = list(range(1, len(data) + 1))  # Increases by 1 for each x-axis point

        label = f"run_timeout = {run_timeout}"
        ax.plot(x_values, y_values, marker='o', linestyle='-', label=label)

    ax.set_xlabel("Runtime")
    ax.set_title("Line plot - Correct cases for tool 'PASDA-diff' sorted by run timeout")
    ax.set_xscale('log')
    ax.grid(True)
    ax.legend()

    # Copy the y-axis to the right side
    ax.yaxis.tick_right()
    ax.yaxis.set_label_position("right")

    # Create a second y-axis on the right side and set its values to match the left y-axis
    ax2 = ax.twinx()
    ax2.set_ylabel("Correct cases")
    ax2.set_yticks(ax.get_yticks())
    ax2.set_yticklabels([int(tick) for tick in ax.get_yticks()])


    # Set the y-axis limits on both sides
    ax.set_ylim(0, 100)
    ax2.set_ylim(0, 100)

    # Show the plot
    plt.show()
