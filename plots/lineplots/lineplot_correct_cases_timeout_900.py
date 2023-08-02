import sqlite3
import matplotlib.pyplot as plt

def generate_plot18():
    # Connect to the SQLite database
    db_path = "C:/Users/mirha/Desktop/plots/sqlite-2023-07-10.db"
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    # Get the distinct tool names available in the "_run_group" table
    cursor.execute("SELECT DISTINCT tool FROM _run_group")
    tools = [row[0] for row in cursor.fetchall()]

    # Specify the run_timeout value for comparison
    run_timeout = 10
    data_sets = {}

    for tool in tools:
        query = f"SELECT avg_result_runtime FROM _run_group WHERE all_correct=1 AND tool='{tool}' AND run_timeout= 900 ORDER BY avg_result_runtime ASC"
        cursor.execute(query)
        data_sets[tool] = cursor.fetchall()

    # Close the database connection
    connection.close()

    # Create x and y values for each data set and plot them separately
    for tool, data in data_sets.items():
        x_values = [row[0] for row in data]
        y_values = list(range(1, len(data) + 1))  # Increases by 1 for each x-axis point

        label = f"{tool}"
        plt.plot(x_values, y_values, marker='o', linestyle='-', label=label)

    plt.xlabel("Runtime")
    plt.ylabel("Correct Cases")
    plt.title("Line plot - Correct cases for each tool when run timeout equals 900")
    plt.grid(True)
    plt.legend()

    # Set the y-axis limits for both y-axes to 0 and 100
    plt.gca().set_ylim(0, 110)
    plt.gca().yaxis.tick_left()

    # Create a twin y-axis on the right side
    ax2 = plt.gca().twinx()

    # Set the y-axis limits for the twin y-axis to 0 and 100
    ax2.set_ylim(0, 110)
    ax2.yaxis.tick_right()

    # Set the label for the twin y-axis


    plt.show()
