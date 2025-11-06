import sqlite3
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OneHotEncoder

# --- Step 1: Create Local Database ---
conn = sqlite3.connect("insurance_claims.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS claims (
    claim_id INTEGER PRIMARY KEY,
    patient_age INTEGER,
    patient_gender TEXT,
    claim_amount REAL,
    diagnosis TEXT,
    procedure TEXT,
    approved INTEGER
)
""")
conn.commit()

# --- Step 2: Function to Add New Claim ---
def add_claim():
    age = int(input("Patient Age: "))
    gender = input("Patient Gender (M/F): ").upper()
    amount = float(input("Claim Amount: "))
    diagnosis = input("Diagnosis: ")
    procedure = input("Procedure: ")

    cursor.execute("""
    INSERT INTO claims (patient_age, patient_gender, claim_amount, diagnosis, procedure, approved)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (age, gender, amount, diagnosis, procedure, None))
    conn.commit()
    print("Claim added successfully!")

# --- Step 3: Function to Train ML Model ---
def train_model():
    df = pd.read_sql_query("SELECT * FROM claims WHERE approved IS NOT NULL", conn)
    if df.empty:
        print("No approved/rejected claims yet. Cannot train model.")
        return None
    
    # Separate features and target
    X = df.drop(['claim_id', 'approved'], axis=1)
    y = df['approved']

    # Convert categorical features
    X = pd.get_dummies(X, columns=['patient_gender', 'diagnosis', 'procedure'], drop_first=True)

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train Random Forest
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    print("Model trained successfully!")
    return model, X.columns  # Return model and columns for consistency

# --- Step 4: Function to Predict New Claim ---
def predict_claim(model, columns):
    df = pd.read_sql_query("SELECT * FROM claims WHERE approved IS NULL", conn)
    if df.empty:
        print("No new claims to predict.")
        return

    X_new = df.drop(['claim_id', 'approved'], axis=1)
    X_new = pd.get_dummies(X_new, columns=['patient_gender', 'diagnosis', 'procedure'], drop_first=True)

    # Align columns
    X_new = X_new.reindex(columns=columns, fill_value=0)

    predictions = model.predict(X_new)
    df['approved'] = predictions

    # Update predictions in database
    for index, row in df.iterrows():
        cursor.execute("""
        UPDATE claims SET approved = ? WHERE claim_id = ?
        """, (row['approved'], row['claim_id']))
    conn.commit()
    print("Predictions updated in the database!")
    print(df[['claim_id', 'approved']])

# --- Step 5: Interactive Menu ---
def main():
    while True:
        print("\n--- Medical Insurance Claims System ---")
        print("1. Add new claim")
        print("2. Train ML model")
        print("3. Predict claim approval")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            add_claim()
        elif choice == '2':
            global model, model_columns
            model, model_columns = train_model()
        elif choice == '3':
            if 'model' not in globals() or model is None:
                print("Train the model first!")
            else:
                predict_claim(model, model_columns)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    model, model_columns = None, None
    main()
    conn.close()
