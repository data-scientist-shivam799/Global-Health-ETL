<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- <title>Health ETL Process</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
            background-color: #f4f4f4;
        }
        h1, h2, h3 {
            color: #333;
        }
        code {
            background-color: #e7e7e7;
            padding: 2px 4px;
            border-radius: 3px;
        }
        pre {
            background-color: #e7e7e7;
            padding: 10px;
            border-radius: 5px;
            overflow-x: auto;
        }
        ul {
            list-style-type: square;
        }
        .project-structure {
            background-color: #e7e7e7;
            padding: 10px;
            border-radius: 5px;
            overflow-x: auto;
        }
    </style> -->
</head>
<body>

<h1>Health ETL Process</h1>

<h2>Overview</h2>
<p>
    The Health ETL (Extract, Transform, Load) process is designed to parse customer data from a text file, validate the data, transform it as necessary, and load it into an SQLite database. This project includes the functionality to create the database schema, validate data entries, and handle various data types, ensuring that the database remains consistent and reliable.
</p>

<h2>Features</h2>
<ul>
    <li><strong>File Parsing:</strong> Reads customer data from a specified text file.</li>
    <li><strong>Data Validation:</strong> Validates and cleans data before insertion into the database.</li>
    <li><strong>Data Transformation:</strong> Calculates derived fields such as age and days since last consultation.</li>
    <li><strong>Database Loading:</strong> Inserts validated and transformed data into an SQLite database.</li>
    <li><strong>Table Creation:</strong> Creates necessary tables in the SQLite database if they do not already exist.</li>
</ul>

<h2>Project Structure</h2>
<div class="project-structure">
<pre>
project-directory/
│
├── src/
│   ├── customer_data.txt          # Input file containing customer data.
│   ├── create_tables.sql          # SQL script to create database tables.
│   ├── create_tables.py           # Python script to execute SQL script.
│   ├── main.py                    # Main ETL process script.
│   └── data_validator.py           # Data validation logic.
│
├── hospital_data.db               # SQLite database file (generated).
└── README.md                      # Project documentation.
</pre>
</div>

<h2>Requirements</h2>
<ul>
    <li>Python 3.x</li>
    <li>SQLite</li>
</ul>

<h2>Installation</h2>
<pre>
1. Clone the repository:
   <code>git clone &lt;repository-url&gt;</code>
   <code>cd project-directory</code>

2. Install any required Python packages (if applicable):
   <code>pip install -r requirements.txt</code>
</pre>

<h2>Database Schema</h2>
<p>The following tables are created in the SQLite database:</p>
<ul>
    <li><strong>Customer:</strong> Stores customer information.</li>
    <li><strong>Doctor:</strong> Contains doctor details.</li>
    <li><strong>Vaccination:</strong> Lists vaccination types.</li>
    <li><strong>Consultation:</strong> Records consultation details.</li>
    <li><strong>Country:</strong> Holds country information.</li>
    <li><strong>Customer_Country_Map:</strong> Maps customers to their respective countries.</li>
</ul>

<h2>Usage</h2>
<h3>Step 1: Create Database Tables</h3>
<p>Run the following command to create the necessary tables in the SQLite database:</p>
<pre>
<code>python src/create_tables.py</code>
</pre>

<h3>Step 2: Run the ETL Process</h3>
<p>After creating the tables, run the ETL process to load data from the text file:</p>
<pre>
<code>python src/main.py</code>
</pre>

<h2>Contributing</h2>
<p>If you would like to contribute to this project, feel free to submit a pull request or create an issue for discussion.</p>

<h2>License</h2>
<p>This project is developed under Incubytein as an assessment project .</p>

</body>
</html>