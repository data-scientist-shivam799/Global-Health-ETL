import sqlite3

def create_tables_from_sql(db_name, sql_file):
    """
    Create tables in the database by executing SQL script from a file.

    Args:
        db_name (str): The name of the database to connect to.
        sql_file (str): The path to the SQL file containing table creation scripts.
    """
    # Open the SQL file and read its contents
    with open(sql_file, 'r') as file:
        sql_script = file.read()

    # Establish a connection to the SQLite database
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    # Execute the SQL script to create tables
    try:
        cursor.executescript(sql_script)
        print("All tables created successfully.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        # Commit changes and close the database connection
        connection.commit()
        connection.close()

if __name__ == "__main__":
    db_name = 'hospital_data.db'
    sql_file = 'src/create_tables.sql'
    create_tables_from_sql(db_name, sql_file)
