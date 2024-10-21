import sqlite3

class DatabaseQuery:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def get_all_customers(self):
        sql = '''SELECT * FROM Customer'''
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get_customer_by_id(self, customer_id):
        sql = '''SELECT * FROM Customer WHERE Customer_Id = ?'''
        self.cursor.execute(sql, (customer_id,))
        return self.cursor.fetchone()

    def get_consultations_by_customer(self, customer_id):
        sql = '''SELECT C.*, D.Doctor_Name, V.Vaccination_Type 
                 FROM Consultation C 
                 LEFT JOIN Doctor D ON C.Doctor_Id = D.Doctor_Id 
                 LEFT JOIN Vaccination V ON C.Vaccination_Id = V.Vaccination_Id 
                 WHERE C.Customer_Id = ?'''
        self.cursor.execute(sql, (customer_id,))
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()

if __name__ == "__main__":
    db_name = 'hospital_data.db'
    query = DatabaseQuery(db_name)

    # Get all customers
    customers = query.get_all_customers()
    print("All Customers:")
    for customer in customers:
        print(customer)

    # Get customer by ID
    customer_id = '123457'  # Example Customer_Id
    customer = query.get_customer_by_id(customer_id)
    print(f"\nCustomer with ID {customer_id}:")
    print(customer)

    # Get consultations for a specific customer
    consultations = query.get_consultations_by_customer(customer_id)
    print(f"\nConsultations for Customer {customer_id}:")
    for consultation in consultations:
        print(consultation)

    query.close()
