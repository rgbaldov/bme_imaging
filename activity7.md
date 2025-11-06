# Activity 7: Medical Insurance Claims Analysis

**Prepared by:**  

[Renann G. Baldovino, PhD](https://www.dlsu.edu.ph/colleges/gcoe/academic-departments/manufacturing-engineering-management/faculty-profile/renann-baldovino/)  
**[Department of Manufacturing Engineering and Management, De La Salle University (DLSU)](https://www.dlsu.edu.ph/colleges/gcoe/academic-departments/manufacturing-engineering-management/)**

## Overview
This example demonstrates:
1. Creating a local database for storing insurance claims.
2. Inserting sample data.
3. Loading data from the database.
4. Performing a simple machine learning task (predicting claim approval).

## How It Works
1. Creates a local SQLite database to store claims.
2. Users can enter new claims interactively via the console.
3. Trains a Random Forest classifier on claims with known approvals.
4. Predicts approval for newly added claims and updates the database.
5. Provides a simple console menu for managing claims and running ML tasks.

## [Python Code](https://raw.githubusercontent.com/rgbaldov/bme_imaging/refs/heads/main/insurance.py)

## Libraries
pip install pandas scikit-learn sqlite3

## Next Steps
1. Add a GUI using Tkinter/Streamlit for better usability.
2. Enable exporting claim data to CSV for reporting or analysis.
