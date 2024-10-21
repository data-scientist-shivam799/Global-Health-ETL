from src.file_module import FileParser
from src.db_module import DatabaseLoader
from src.helpers import DataTransformer, DataValidator

class ETLProcess:
    def __init__(self, file_path, db_name, current_date):
        """
        Initialize the ETL process with the specified file path, database name, and current date.

        Args:
            file_path (str): The path to the input data file.
            db_name (str): The name of the database to connect to.
            current_date (str): The current date, used for transformations, in the format %Y%m%d.
        """
        # Store the file path for the input data
        self.file_path = file_path

        # Store the name of the database
        self.db_name = db_name

        # Store the current date for transformations
        self.current_date = current_date

    def run(self):
        """
        Run the ETL process.

        This method parses the specified file, transforms and validates the data, and then loads it into the database.
        """
        # Step 1: Parse the file
        parser = FileParser(self.file_path)
        header, details = parser.parse_file()

        # Step 2: Transform and validate each row
        transformer = DataTransformer(self.current_date)
        validator = DataValidator()
        db_loader = DatabaseLoader(self.db_name)

        for detail in details:
            # Validate the row
            validated_row = validator.validate(detail)

            # Calculate derived fields
            age = transformer.calculate_age(validated_row[9])  # DOB is at index 9
            days_since_consultation = transformer.days_since_last_consultation(validated_row[4])  # Last consultation at index 4

            # Insert customer data
            customer_data = (validated_row[2], validated_row[1], validated_row[9], validated_row[10])  # Customer_Id, Customer_Name, DOB, Is_Active
            db_loader.insert_customer(customer_data)

            # Insert consultation data
            consultation_data = (validated_row[2], 1, validated_row[5], validated_row[2], validated_row[4], validated_row[6], validated_row[7], days_since_consultation)
            db_loader.insert_consultation(consultation_data)

            # Insert country mapping data
            country_mapping = (validated_row[1], validated_row[7])  # Customer_Id, Country_Code
            db_loader.insert_country_mapping(country_mapping)

        # Close the database connection when done
        db_loader.close()

# Example usage
if __name__ == "__main__":
    etl = ETLProcess('src/customer_data.txt', 'hospital_data.db', '20241021')
    etl.run()
