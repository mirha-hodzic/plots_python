import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

def generate_plot20():

    # Verbindung zur Datenbank herstellen
    db_path = "C:/Users/mirha/desktop/plots/sqlite-2023-07-10.db"
    connection = sqlite3.connect(db_path)

    # Funktion zum Abrufen der Daten aus der Datenbank für den angegebenen Timeout
    def get_data(tool, expected, timeout):
        query = f"""
            SELECT avg_result_runtime
            FROM _run_group
            WHERE tool = '{tool}' AND expected = '{expected}' AND run_timeout = {timeout} ORDER BY avg_result_runtime ASC
        """
        data = pd.read_sql_query(query, connection)
        return data["avg_result_runtime"].tolist()

    # Timeout-Wert festlegen
    timeout = 10

    # Daten für ARDiff-base:EQ, ARDiff-base:NEQ, PASDA-diff:EQ und PASDA-diff:NEQ abrufen
    ardiff_eq = get_data("ARDiff-base", "EQ", timeout)
    ardiff_neq = get_data("ARDiff-base", "NEQ", timeout)
    pasda_eq = get_data("PASDA-diff", "EQ", timeout)
    pasda_neq = get_data("PASDA-diff", "NEQ", timeout)


    fig, ax = plt.subplots()

    for label, data in {"ARDiff-base:EQ":ardiff_eq, "ARDiff-base:NEQ":ardiff_neq, "PASDA-diff:EQ":pasda_eq, "PASDA-diff:NEQ":pasda_neq}.items():
        x_values = data
        y_values = list(range(1, len(data) + 1))  # Increases by 1 for each x-axis point
        ax.plot(x_values, y_values, marker='o', linestyle='-', label=label)

    plt.xlabel("Runtime")
    plt.ylabel("Processed Cases")  # Hier wird die y-Achse beschriftet

    plt.title(f"Line plot - Correct cases for tool 'ARDiff-base' and 'PASDA-diff' sorted by (Timeout = {timeout})")
    plt.grid(True)
    plt.legend()


    # Plot anzeigen
    plt.show()

    # Verbindung zur Datenbank schließen
    connection.close()
