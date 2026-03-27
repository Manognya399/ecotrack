import sqlite3
import os

conn = sqlite3.connect("backend/ecotrack.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS vendors (
    id INTEGER PRIMARY KEY,
    name TEXT,
    carbon_per_shipment REAL,
    certification TEXT,
    cert_year INTEGER,
    on_time_eco_deliveries INTEGER,
    total_deliveries INTEGER
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS shipments (
    id INTEGER PRIMARY KEY,
    vendor_id INTEGER,
    route TEXT,
    carbon_emitted REAL,
    date TEXT,
    status TEXT
)
''')

vendors = [
    (1, "GreenMile Pvt Ltd", 12.4, "ISO14001", 2023, 45, 50),
    (2, "NovaTrans Logistics", 38.7, "None", 2020, 10, 50),
    (3, "EcoFreight India", 9.1, "CarbonNeutral", 2024, 48, 50),
    (4, "FastHaul Co", 55.2, "None", 2019, 5, 50),
    (5, "ClearPath Carriers", 21.3, "ISO14001", 2022, 30, 50),
    (6, "BlueSky Freight", 44.8, "Expired", 2021, 15, 50),
]

shipments = [
    (1, 1, "Mumbai-Delhi", 11.2, "2024-01-10", "delivered"),
    (2, 1, "Delhi-Chennai", 13.1, "2024-01-15", "delivered"),
    (3, 2, "Mumbai-Kolkata", 40.3, "2024-01-12", "delivered"),
    (4, 3, "Chennai-Hyderabad", 8.9, "2024-01-18", "delivered"),
    (5, 3, "Hyderabad-Pune", 9.4, "2024-01-20", "delivered"),
    (6, 4, "Delhi-Mumbai", 57.1, "2024-01-22", "delivered"),
    (7, 5, "Pune-Bangalore", 20.8, "2024-01-25", "delivered"),
    (8, 6, "Kolkata-Delhi", 46.2, "2024-01-28", "delivered"),
    (9, 2, "Chennai-Mumbai", 37.4, "2024-02-01", "delivered"),
    (10, 4, "Bangalore-Hyderabad", 53.8, "2024-02-03", "delivered"),
]

cursor.executemany("INSERT OR IGNORE INTO vendors VALUES (?,?,?,?,?,?,?)", vendors)
cursor.executemany("INSERT OR IGNORE INTO shipments VALUES (?,?,?,?,?,?)", shipments)

conn.commit()
conn.close()
print("Database seeded successfully!")