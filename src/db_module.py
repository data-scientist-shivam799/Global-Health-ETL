import sqlite3

class DatabaseLoader:
    def __init__(self, db_name):
        """
        Initialize the database loader with a connection to the specified database.

        Args:
            db_name (str): The name of the database to connect to.
        """
        # Establish a connection to the SQLite database
        self.connection = sqlite3.connect(db_name)
        
        # Create a cursor object to execute SQL commands
        self.cursor = self.connection.cursor()

    def insert_customer(self, customer_data):
        """
        Insert a customer record into the database if it doesn't already exist.

        Args:
            customer_data (tuple): A tuple containing the customer's ID, name, date of birth and activity status.
        """
        sql = '''INSERT OR IGNORE INTO Customer (Customer_Id, Customer_Name, DOB, Is_Active) 
                 VALUES (?, ?, ?, ?)'''
        # Execute the SQL command with the customer data
        self.cursor.execute(sql, customer_data)
        
        # Commit the changes to the database
        self.connection.commit()

    def insert_consultation(self, consultation_data):
        """
        Insert a consultation record into the database.

        Args:
            consultation_data (tuple): A tuple containing the consultation details including
                                       Customer_Id, Doctor_Id, Vaccination_Id, Open_Date, 
                                       Last_Consulted_Date, State, Country, and Days_Since_Last_Consultation.
        """
        # SQL command to insert a new consultation record
        sql = '''INSERT INTO Consultation (Customer_Id, Doctor_Id, Vaccination_Id, Open_Date, 
                                           Last_Consulted_Date, State, Country, Days_Since_Last_Consultation) 
                 VALUES (?, ?, ?, ?, ?, ?, ?, ?)'''
        # Execute the SQL command with the provided consultation data
        self.cursor.execute(sql, consultation_data)
        
        # Commit the changes to the database to save the new record
        self.connection.commit()

    def insert_country_mapping(self, mapping_data):
        """
        Insert a country mapping record into the database.

        Args:
            mapping_data (tuple): A tuple containing the Customer_Id and Country_Code.
        """
        # SQL command to insert a new country mapping record
        sql = '''INSERT INTO Customer_Country_Map (Customer_Id, Country_Code) 
                 VALUES (?, ?)'''
        # Execute the SQL command with the provided mapping data
        self.cursor.execute(sql, mapping_data)
        
        # Commit the changes to the database to save the new record
        self.connection.commit()

    def close(self):
        """
        Close the database connection.

        This method ensures that the connection to the database
        is properly closed to free up resources.
        """
        # Close the connection to the database
        self.connection.close()