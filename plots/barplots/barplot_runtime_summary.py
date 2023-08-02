import matplotlib.pyplot as plt
import sqlite3
import numpy as np

def generate_plot1(): 


    # Connect to the SQLite database
    conn = sqlite3.connect('C:/Users/mirha/Desktop/plots/sqlite-2023-07-10.db')

    # Execute a query to retrieve the data
    cursor = conn.execute('SELECT * FROM _run_group_result_list')

    # Extract the data from the cursor
    data = cursor.fetchall()

    # Close the database connection
    conn.close()

    # Create the bar chart

    categories = [f"{row[0]} - {row[2]} - {row[1]}" for row in data]
    values = [row[3] for row in data]



    plt.bar(categories, values, color="orange")
    plt.xlabel('Tool used')
    plt.ylabel('Average Runtime (Seconds)')
    plt.title('Runtime Summary')
    plt.xticks(range(len(categories)), categories, rotation='vertical')
    plt.show()  

    #bar2

    conn = sqlite3.connect('C:/Users/mirha/Desktop/plots/sqlite-2023-07-10.db')

    # Execute a query to retrieve the data
    cursor = conn.execute('SELECT * FROM _run_group_result_list')

    # Extract the data from the cursor
    data = cursor.fetchall()

    # Close the database connection
    conn.close()

    # Create the bar chart

    categories = [f"{row[0]} - {row[2]} - {row[1]}" for row in data]
    values = [row[9] for row in data]

    plt.bar(categories, values, color="pink")
    plt.xlabel('Tool used')
    plt.ylabel('Correct Cases')
    plt.title('Correct Cases')
    plt.xticks(range(len(categories)), categories, rotation='vertical')
    plt.show()

if __name__ == "__main__":
    generate_plot1()

