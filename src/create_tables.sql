-- Customer Table
CREATE TABLE Customer (
    Customer_Id VARCHAR(18) PRIMARY KEY,
    Customer_Name VARCHAR(255) NOT NULL,
    DOB DATE NOT NULL,
    Is_Active CHAR(1) CHECK (Is_Active IN ('A', 'I')) NOT NULL
);

-- Doctor Table
CREATE TABLE Doctor (
    Doctor_Id SERIAL PRIMARY KEY,
    Doctor_Name VARCHAR(255) NOT NULL
);

-- Vaccination Table
CREATE TABLE Vaccination (
    Vaccination_Id CHAR(5) PRIMARY KEY,
    Vaccination_Type VARCHAR(100)
);

-- Consultation Table
CREATE TABLE Consultation (
    Consultation_Id SERIAL PRIMARY KEY,
    Customer_Id VARCHAR(18) NOT NULL,
    Doctor_Id INT NOT NULL,
    Vaccination_Id CHAR(5),
    Open_Date DATE NOT NULL,
    Last_Consulted_Date DATE,
    State CHAR(5),
    Country CHAR(5),
    Days_Since_Last_Consultation INT,
    
    FOREIGN KEY (Customer_Id) REFERENCES Customer(Customer_Id),
    FOREIGN KEY (Doctor_Id) REFERENCES Doctor(Doctor_Id),
    FOREIGN KEY (Vaccination_Id) REFERENCES Vaccination(Vaccination_Id)
);

-- Country Table
CREATE TABLE Country (
    Country_Code CHAR(5) PRIMARY KEY,
    Country_Name VARCHAR(100) NOT NULL
);

-- Customer Country Mapping Table
CREATE TABLE Customer_Country_Map (
    Map_Id SERIAL PRIMARY KEY,
    Customer_Id VARCHAR(18) NOT NULL,
    Country_Code CHAR(5) NOT NULL,
    
    FOREIGN KEY (Customer_Id) REFERENCES Customer(Customer_Id),
    FOREIGN KEY (Country_Code) REFERENCES Country(Country_Code)
);
