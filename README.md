\# Data Processing Pipeline



\## 📌 Project Overview



This project implements a simple and reliable data processing pipeline using Python and Pandas.



The pipeline reads raw student data from a CSV file, checks for missing values, cleans the data, converts data types, creates a student performance status, and saves the processed data.



\## 🔄 Pipeline Flow



Raw CSV Data  

↓  

Read Data  

↓  

Check Missing Values  

↓  

Clean Missing Values  

↓  

Convert Data Types  

↓  

Create Pass/Fail Status  

↓  

Save Processed Data  

↓  

Generate Logs



\## 📁 Project Structure



```text

Data\_Processing\_Pipeline/

│

├── input/

│   └── students.csv

│

├── output/

│   └── processed\_students.csv

│

├── src/

│   └── pipeline.py

│

├── logs/

│   └── pipeline.log

│

├── config.json

├── requirements.txt

└── README.md

