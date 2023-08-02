import sqlite3
import matplotlib.pyplot as plt

# Verbindung zur Datenbank herstellen
db_path = "C:/Users/mirha/Desktop/plots/sqlite-2023-07-10.db"
connection = sqlite3.connect(db_path)
cursor = connection.cursor()

def generate_plot27():

    # Die SQL-Abfrage ausführen
    query = f"""
    SELECT run_timeout, result, COUNT(*) FROM _run_group_result
    WHERE tool = 'PASDA-diff' GROUP BY run_timeout, result
    """
    cursor.execute(query)

    # Daten aus der Datenbank abrufen und in einem geeigneten Format speichern
    data = cursor.fetchall()

    run_timeouts = set()
    results = set()
    data_dict = {}

    # Nur die gewünschten Ergebnisse berücksichtigen
    desired_results = ["DEPTH_LIMITED", "EQ", "NEQ", "MAYBE_EQ", "MAYBE_NEQ", "UNKNOWN", "TIMEOUT", "ERROR"]

    for row in data:
        run_timeout, result, count = row
        if result in desired_results:
            run_timeouts.add(run_timeout)
            results.add(result)
            
            if run_timeout not in data_dict:
                data_dict[run_timeout] = {result: count}
            else:
                data_dict[run_timeout][result] = count

    # Sortiere die run_timeouts
    sorted_run_timeouts = sorted(run_timeouts)

    # Bar-Chart erstellen
    fig, ax = plt.subplots()
    width = 0.1
    x_positions = range(len(sorted_run_timeouts))

    for i, result in enumerate(desired_results):
        if result in results:  # Nur hinzufügen, wenn das Ergebnis in den abgerufenen Daten vorhanden ist
            counts = [data_dict[run_timeout].get(result, 0) for run_timeout in sorted_run_timeouts]
            ax.bar(x_positions, counts, width, label=result)
            x_positions = [pos + width for pos in x_positions]  # Move the x_positions for the next bar group



    # Achsenbeschriftungen und Legende hinzufügen
    ax.set_xlabel('Timeout')
    ax.set_ylabel('Processed Cases')
    ax.set_title('Barplot: Processed cases for tool "PASDA-diff" sorted by timeout')

    # Calculate the centering offset for the x-axis labels
    center_offset = width * (len(desired_results) - 1) / 2
    ax.set_xticks([pos + center_offset for pos in range(len(sorted_run_timeouts))])  # Hier werden die X-Positionen angepasst

    ax.set_xticklabels(sorted_run_timeouts)
    ax.legend()

    # Diagramm anzeigen oder speichern
    plt.tight_layout()
    plt.grid()
    plt.show()
