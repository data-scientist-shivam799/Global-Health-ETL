-- Query the Data
SELECT 
    c.Customer_Name,
    c.DOB,
    d.Doctor_Name,
    v.Vaccination_Type,
    cn.Country_Name,
    con.Last_Consulted_Date,
    con.Days_Since_Last_Consultation
FROM 
    Customer c
JOIN 
    Consultation con ON c.Customer_Id = con.Customer_Id
JOIN 
    Doctor d ON con.Doctor_Id = d.Doctor_Id
JOIN 
    Vaccination v ON con.Vaccination_Id = v.Vaccination_Id
JOIN 
    Customer_Country_Map cm ON c.Customer_Id = cm.Customer_Id
JOIN 
    Country cn ON cm.Country_Code = cn.Country_Code
WHERE 
    cn.Country_Code = 'IND';