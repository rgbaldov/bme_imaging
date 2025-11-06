import sqlite3
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

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

# --- Step 2: Insert Sample Data ---
sample_data = [
    (25, 'M', 1200.50, 'Fracture', 'X-ray', 1),
    (40, 'F', 3000.00, 'Heart Disease', 'Angiography', 1),
    (60, 'M', 5000.00, 'Cancer', 'Chemotherapy', 0),
    (35, 'F', 1500.00, 'Flu', 'Medication', 1),
    (50, 'M', 4000.00, 'Diabetes', 'Insulin Therapy', 1),
    (28, 'F', 2000.00, 'Appendicitis', 'Surgery', 0),
]

cursor.executemany("""
INSERT INTO claims (patient_age, patient_gender, claim_amount, diagnosis, procedure, approved)
VALUES (?, ?, ?, ?, ?, ?)
""", sample_data)
conn.commit()

# --- Step 3: Load Data into Pandas ---
df = pd.read_sql_query("SELECT * FROM claims", conn)
print("Data from Database:")
print(df)

# Convert categorical data
df = pd.get_dummies(df, columns=['patient_gender', 'diagnosis', 'procedure'], drop_first=True)

# --- Step 4: Machine Learning: Predict Claim Approval ---
X = df.drop(['claim_id', 'approved'], axis=1)
y = df['approved']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

# --- Step 5: Evaluation ---
print("\nAccuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Close the database connection
conn.close()
