import sqlite3

def clear_database(db_name):
    """
    Clear the database by dropping all tables.
    """
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    # List of tables to drop
    tables = [
        "Customer_Country_Map",
        "Consultation",
        "Vaccination",
        "Doctor",
        "Country",
        "Customer"
    ]

    # Drop each of the tables if they exist
    for table in tables:
        # Construct the DROP TABLE SQL command
        sql = f"DROP TABLE IF EXISTS {table}"
        # Execute the SQL command
        cursor.execute(sql)

    # Commit the changes to the database
    connection.commit()
    # Close the connection to the database
    connection.close()
    print("All tables dropped and database cleared.")

if __name__ == "__main__":
    db_name = 'hospital_data.db'
    clear_database(db_name)