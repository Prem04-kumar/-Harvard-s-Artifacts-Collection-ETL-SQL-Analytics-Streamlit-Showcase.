# 🏛️ Harvard's Artifacts Collection: ETL, SQL Analytics & Streamlit Showcase
 
### End-to-End Data Engineering Project using Harvard Art Museums API
 
![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)
![Harvard API](https://img.shields.io/badge/Harvard%20Art%20Museums-API-A51C30?style=for-the-badge)
 
---
 
## 📘 Table of Contents
 
- [Overview](#-overview)
- [Features](#-features)
- [Architecture](#-architecture)
- [Tech Stack](#-tech-stack)
- [Database Schema](#-database-schema)
- [Project Structure](#-project-structure)
- [ETL Pipeline Workflow](#-etl-pipeline-workflow)
- [App Workflow](#-app-workflow)
- [SQL Queries](#-sql-queries-20-included)
- [Setup & Run](#-setup--run)
- [Future Enhancements](#-future-enhancements)
- [Author](#-author)
---
 
## 📌 Overview
 
This project is a complete **ETL + SQL Analytics + Streamlit Dashboard** solution built on top of the **Harvard Art Museums public API**.
 
It enables users to:
- Dynamically **fetch up to 2,500 artifact records** per classification from Harvard's digital archive
- Run a full **ETL pipeline** to clean, normalize, and store the data in MySQL Cloud
- Explore art collections interactively through a **Streamlit web application**
- Execute **20 analytical SQL queries** to derive insights across periods, departments, and color profiles
> Built as an **end-to-end Data Engineering portfolio project** combining API integration, ETL design, relational database management, and interactive deployment.
 
---
 
## 🚀 Features
 
| Feature | Description |
|---------|-------------|
| 🌐 API Ingestion | Fetch up to **2,500 artifact records** per classification from the Harvard Art Museums API |
| 🔄 ETL Pipeline | Full Extract → Transform → Load pipeline for Metadata, Media, and Color datasets |
| 🧹 Data Cleaning | Normalize and clean raw API responses before database insertion |
| 🗄️ MySQL Cloud Storage | Store structured data in **3 relational tables** with primary & foreign keys |
| 🔒 Duplicate-Safe Insertion | SQL insertion logic using primary key constraints to avoid duplicates |
| 🌐 Streamlit Dashboard | Interactive UI for live data preview and query execution |
| 🔢 SQL Analytics | **20 analytical queries** covering metadata, media, colors, joins, and rankings |
 
---
 
## 🏗️ Architecture
 
```
Harvard Art Museums API
          ↓
   Data Extraction (harvard_project.ipynb)
          ↓
   ETL Processing & Cleaning (Pandas)
          ↓
   MySQL Cloud Database (3 Tables)
          ↓
   Streamlit Web Application (har.py)
          ↓
   SQL Query Execution & Analytics (harvard.sql)
          ↓
   Interactive Results & Insights
```
 
---
 
## 🧰 Tech Stack
 
| Category | Tools |
|----------|-------|
| Language | Python 3.8+ |
| Web App | Streamlit |
| Database | MySQL Cloud |
| Data Processing | Pandas |
| API Integration | Harvard Art Museums Public API |
| Queries | SQL (20 analytical queries) |
| Environment | Jupyter Notebook |
 
---
 
## 🗄️ Database Schema
 
The project uses **3 relational tables** in MySQL:
 
### 1. `artifact_metadata`
Stores core information about each artifact.
 
| Column | Type | Description |
|--------|------|-------------|
| `id` | INT (PK) | Unique artifact identifier |
| `title` | VARCHAR | Artifact title |
| `culture` | VARCHAR | Cultural origin |
| `period` | VARCHAR | Historical period |
| `century` | VARCHAR | Century of origin |
| `medium` | TEXT | Material/medium used |
| `dimensions` | TEXT | Physical dimensions |
| `description` | TEXT | Artifact description |
| `department` | VARCHAR | Museum department |
| `classification` | VARCHAR | Artifact classification |
| `accessionyear` | INT | Year acquired |
| `accessionmethod` | VARCHAR | How it was acquired |
 
---
 
### 2. `artifact_media`
Stores media and date information linked to artifacts.
 
| Column | Type | Description |
|--------|------|-------------|
| `objectid` | INT (FK → metadata.id) | Reference to artifact |
| `imagecount` | INT | Number of images |
| `mediacount` | INT | Number of media files |
| `colorcount` | INT | Number of color profiles |
| `rank` | INT | Popularity rank |
| `datebegin` | INT | Start date of artifact |
| `dateend` | INT | End date of artifact |
 
---
 
### 3. `artifact_colors`
Stores dominant color data extracted from artifact images.
 
| Column | Type | Description |
|--------|------|-------------|
| `objectid` | INT (FK → metadata.id) | Reference to artifact |
| `color` | VARCHAR | Dominant color name |
| `spectrum` | VARCHAR | Color spectrum value |
| `hue` | VARCHAR | Hue category |
| `percent` | FLOAT | Percentage of image covered |
| `css3` | VARCHAR | CSS3 color code |
 
---
 
## 📁 Project Structure
 
```
Harvard-Artifacts-Project/
│
├── harvard_project.ipynb    # API integration, data extraction & ETL pipeline
├── har.py                   # Main Streamlit UI application
├── harvard.sql              # All 20 SQL analytical queries
└── README.md                # Project documentation
```
 
---
 
## 🔄 ETL Pipeline Workflow
 
### Step 1️⃣ — Extract
- Connect to **Harvard Art Museums API**
- Select a classification (e.g., Paintings, Sculpture, Coins)
- Paginate and fetch up to **2,500 artifact records**
### Step 2️⃣ — Transform
- Parse raw JSON API responses
- Extract relevant fields into structured DataFrames:
  - `Metadata DataFrame` — artifact info
  - `Media DataFrame` — image/media counts & dates
  - `Colors DataFrame` — dominant color profiles
- Handle missing values, nulls, and data type conversions
- Normalize and flatten nested fields
### Step 3️⃣ — Load
- Connect to **MySQL Cloud** database
- Create tables if they don't exist
- Insert records with **duplicate-safe logic** (primary key enforcement)
- Load all 3 DataFrames into their respective tables
---
 
## 🧭 App Workflow
 
The Streamlit app (`har.py`) guides users through the full pipeline:
 
```
1. Select Classification (Paintings / Sculpture / Coins / etc.)
        ↓
2. Collect 2,500 Records via API
        ↓
3. View 3-Section Data Preview
   (Metadata | Media | Colors)
        ↓
4. Migrate to SQL → Insert into 3 Tables
        ↓
5. Select & Run SQL Queries (1–20)
        ↓
6. View Results Interactively in Dashboard
```
 
---
 
## 🔢 SQL Queries (20 Included)
 
All queries are stored in `harvard.sql` and executable directly from the Streamlit app:
 
| Category | Queries |
|----------|---------|
| 📋 Metadata Filters | Filter by culture, period, century, department, classification |
| 🖼️ Media Analysis | Rank by image count, media richness, and artifact popularity |
| 🎨 Color Analytics | Most common hues, dominant colors, color percentage distribution |
| 🔗 Multi-table Joins | Join metadata + media + colors for comprehensive artifact profiles |
| 📊 Classification Insights | Count and group artifacts by classification and department |
| 🏆 Ranking-Based Results | Top artifacts by rank, date range, and accession year |
 
---
 
## ⚙️ Setup & Run
 
### 1. Clone the Repository
 
```bash
git clone https://github.com/Prem04-kumar/-Harvard-s-Artifacts-Collection-ETL-SQL-Analytics-Streamlit-Showcase..git
cd -Harvard-s-Artifacts-Collection-ETL-SQL-Analytics-Streamlit-Showcase.
```
 
### 2. Install Dependencies
 
```bash
pip install streamlit pandas mysql-connector-python requests jupyter
```
 
### 3. Configure MySQL Connection
 
Update your MySQL Cloud credentials in `har.py` and `harvard_project.ipynb`:
 
```python
host     = "your-mysql-host"
user     = "your-username"
password = "your-password"
database = "harvard_artifacts"
```
 
### 4. Get Harvard API Key
 
Register for a free API key at [Harvard Art Museums API](https://harvardartmuseums.org/collections/api) and add it to your notebook/app config.
 
### 5. Run ETL Notebook (First-Time Setup)
 
```bash
jupyter notebook harvard_project.ipynb
```
 
Run all cells to extract data from the API and load it into MySQL.
 
### 6. Launch the Streamlit App
 
```bash
streamlit run har.py
```
 
Open your browser at `http://localhost:8501` and start exploring Harvard's art collection!
 
---
 
## 📊 Key Insights from SQL Analytics
 
- 🎨 Dominant colors across artifact collections reveal era-specific aesthetic trends
- 🏛️ Certain departments hold disproportionately high-ranked artifacts by media richness
- 📅 Accession year analysis shows acquisition surges during specific historical periods
- 🌍 Culture-based filters expose geographic diversity in Harvard's global collection
- 🖼️ Artifacts with higher image counts correlate with higher museum popularity ranks
---
 
## 🌐 Future Enhancements
 
- [ ] 🔍 Add **full-text search** across artifact titles and descriptions
- [ ] 🖼️ Display **artifact images** inline within the Streamlit dashboard
- [ ] 📊 Add **Power BI / Plotly** dashboard for advanced visual analytics
- [ ] ☁️ Deploy Streamlit app on **Streamlit Cloud or AWS**
- [ ] 🤖 Integrate **NLP-based artifact description analysis**
- [ ] 📥 Add **CSV/Excel export** of query results
- [ ] 🔄 Schedule **automated API refresh** for latest artifact data
---
 
## 📚 Key Learnings
 
- ✅ REST API integration with pagination and rate handling
- ✅ End-to-end ETL pipeline design (Extract → Transform → Load)
- ✅ Relational database schema design with FK constraints
- ✅ Duplicate-safe SQL insertion techniques
- ✅ Streamlit app development and deployment
- ✅ 20 multi-table SQL analytical queries
- ✅ Data normalization and cleaning from nested JSON
- ✅ MySQL Cloud database management
---
 
## 👨‍💻 Author
 
**Prem Kumar A**
 
[![GitHub](https://img.shields.io/badge/GitHub-Prem04--kumar-181717?style=for-the-badge&logo=github)](https://github.com/Prem04-kumar)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/)
 
> 📁 Project Type: **Data Engineering | ETL Pipeline | SQL Analytics | API Integration | Streamlit Deployment**
 
---
 
## 📌 Conclusion
 
This project demonstrates a complete **Data Engineering workflow** — from live API data ingestion through an ETL pipeline to a fully interactive Streamlit dashboard with SQL-powered analytics.
 
| Pillar | Contribution |
|--------|-------------|
| 🌐 API Integration | Live data from Harvard Art Museums (2,500 records/run) |
| 🔄 ETL Pipeline | Clean, normalize, and load 3 relational datasets |
| 🗄️ SQL Analytics | 20 queries for metadata, media, color, and ranking insights |
| 🌐 Streamlit App | Interactive UI for exploration and query execution |
| 🏛️ Domain | Digital Humanities + Data Engineering |
 
> By combining the Harvard Art Museums API with a robust ETL pipeline, MySQL backend, and Streamlit frontend, this project showcases how **data engineering** can make cultural heritage data **accessible, queryable, and insightful**.
 
---
 
> ⭐ **If you found this project helpful, please give it a star on GitHub!**

