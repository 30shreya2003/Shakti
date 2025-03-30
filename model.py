import pandas as pd
import sqlite3
import numpy as np
from sklearn.cluster import DBSCAN

# Load the dataset
df = pd.read_csv("repeat_offenders.csv")

# SQLite Integration
conn = sqlite3.connect("offenders.db")
cursor = conn.cursor()

# Create SQLite Table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS complaints (
        Offender_ID TEXT,
        Name TEXT,
        Crime_Type TEXT,
        Date TEXT,
        Location TEXT,
        Complaint_Text TEXT,
        Case_Status TEXT
    )
""")

# Insert data into SQLite database
df.to_sql("complaints", conn, if_exists="replace", index=False)

# Generate synthetic latitude/longitude data for clustering (for demo purposes)
df["Latitude"] = np.random.uniform(-90, 90, len(df))
df["Longitude"] = np.random.uniform(-180, 180, len(df))

coords = np.array(df[["Latitude", "Longitude"]])
dbscan = DBSCAN(eps=10, min_samples=2).fit(coords)
df["Cluster"] = dbscan.labels_

# Close the database connection
conn.close()
