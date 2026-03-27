import sqlite3

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
]

cursor.executemany("INSERT OR IGNORE INTO vendors VALUES (?,?,?,?,?,?,?)", vendors)

conn.commit()
conn.close()

print("Database created!")