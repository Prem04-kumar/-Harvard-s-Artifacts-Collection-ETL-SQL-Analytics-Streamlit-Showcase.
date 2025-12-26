🏛️ Harvard’s Artifacts Collection: ETL, SQL Analytics & Streamlit Showcase
End-to-End Data Engineering Project using Harvard Art Museums API
📘 Table of Contents
Overview
Features
Architecture
Tech Stack
Database Schema
Project Structure
Setup Instructions
Running the Application
App Workflow
SQL Queries (20 Included)

Author
📌 Overview
This project is a complete ETL + SQL Analytics + Streamlit Dashboard solution built using the Harvard Art Museums API.
It enables users to fetch 2500 artifacts per classification, clean & normalize data, store it into MySQL, and run 20 analytical SQL queries inside an interactive dashboard.

🚀 Features
Implemented  API data ingestion to fetch up to 2,500 artifact records from the Harvard Art Museums API
Designed and executed an ETL pipeline to extract, transform, and load Metadata, Media, and Color datasets
Performed data cleaning and normalization before database insertion
Stored processed data in MySQL Cloud with structured relational schemas
Applied duplicate-safe SQL insertion logic using primary keys and constraints
Developed a Streamlit-based user interface for interactive data exploration
Enabled live data preview of artifacts directly from the database
Wrote and executed 20 SQL analytical queries to generate insights across periods, classifications, and departments

🏗 Architecture
Harvard Art Museums API
        ↓
 Data Extraction
        ↓
ETL Processing & Cleaning
        ↓
MySQL Cloud Database
        ↓
Streamlit Web Application
        ↓
SQL Query & Analytics Execution

🧰 Tech Stack
Python, Streamlit
MySQL , Pandas
Harvard Art Museums API
🗄 Database Schema
1. artifact_metadata
Stores general information about artifacts.
id (Primary Key)
title
culture
period
century
medium
dimensions
description
department
classification
accessionyear
accessionmethod
2. artifact_media
objectid (FK → metadata.id)
imagecount
mediacount
colorcount
rank
datebegin
dateend
3. artifact_colors
objectid (FK → metadata.id)
color
spectrum
hue
percent
css3

📁 Project Structure
Harvard-Artifacts-Project/
└── 📘 README.md → Project documentation
├── 🔐 harvard_project.ipynb → API Integration & Data Extraction + Data Transformation (ETL)
├── 🗃 harvard.sql → All 25 SQL queries stored clearly
├── 📄 har.py → Main Streamlit UI Application

▶️ Running the interactive Dashboard
streamlit run har.py
🧭 App Workflow
Select classification
Collect 2500 records
View 3-section data preview
Migrate to SQL
Insert into 3 tables
Run SQL queries
View results
🧮 SQL Queries (20 Included)
Queries include:

Metadata filters
Media analysis
Color analytics
Multi-table joins
Classification insights
Ranking-based results

👨‍💻 Author
Prem Kumar.A
Data Engineering | ETL | SQL | API Integrations



