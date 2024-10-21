from datetime import datetime

class DataTransformer:
    def __init__(self, current_date):
        """
        Initialize the data transformer with the current date.

        This is used to calculate the days since the last consultation and
        the age of the customer.

        Args:
            current_date (str): The current date, in the format %Y%m%d.
        """
        self.current_date = datetime.strptime(current_date, "%Y%m%d")

    def calculate_age(self, dob):
        """
        Calculate the age of the customer based on the current date and the date of birth.

        Args:
            dob (str): The date of birth in the format %d%m%Y.

        Returns:
            int: The calculated age of the customer.
        """
        # Parse the date of birth
        dob_date = datetime.strptime(dob, "%d%m%Y")

        # Calculate the age
        age = self.current_date.year - dob_date.year

        # Return the calculated age
        return age

    def days_since_last_consultation(self, last_consult_date):
        """
        Calculate the number of days since the customer's last consultation.

        Args:
            last_consult_date (str): The date of the customer's last consultation, in the format %Y%m%d.

        Returns:
            int: The number of days since the customer's last consultation.
        """
        # Parse the last consultation date
        last_date = datetime.strptime(last_consult_date, "%Y%m%d")

        # Calculate the delta between the current date and the last consultation date
        delta = self.current_date - last_date

        # Return the days since the last consultation
        return delta.days
    
class DataValidator:
    def validate(self, row):
        """
        Validate and clean a data row.

        This method trims whitespace from each field, ensures that the
        Customer_Name does not exceed 255 characters, and converts the
        Customer_Id to an integer if it is not already.

        Args:
            row (list[str]): A list of strings representing a data row.

        Returns:
            list[str]: A list of cleaned and validated data fields.
        """
        # Trim whitespace from all fields
        row = [field.strip() for field in row]

        # Truncate Customer_Name if it exceeds 255 characters
        if len(row[1]) > 255:
            row[1] = row[1][:255]

        # Convert Customer_Id to integer if not already a digit
        if not row[2].isdigit():
            row[2] = int(row[2])

        # Return the cleaned row
        return row