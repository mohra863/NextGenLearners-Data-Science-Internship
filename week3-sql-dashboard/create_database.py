import sqlite3

# Step 1 — Create the database
conn = sqlite3.connect("nextgen.db")
cursor = conn.cursor()

# Enable foreign key constraints
cursor.execute("PRAGMA foreign_keys = ON")

# Step 2 — Create applicants table
cursor.execute("""
CREATE TABLE IF NOT EXISTS applicants (
    applicant_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    domain TEXT NOT NULL,
    university TEXT,
    application_date TEXT,
    status TEXT
)
""")

# Step 3 — Create interns table
cursor.execute("""
CREATE TABLE IF NOT EXISTS interns (
    intern_id INTEGER PRIMARY KEY,
    applicant_id INTEGER UNIQUE,
    domain TEXT NOT NULL,
    start_date TEXT,
    completion_status TEXT,
    FOREIGN KEY (applicant_id)
        REFERENCES applicants(applicant_id)
)
""")

# Step 4 — Create hackathon_scores table
cursor.execute("""
CREATE TABLE IF NOT EXISTS hackathon_scores (
    intern_id INTEGER PRIMARY KEY,
    score REAL,
    domain TEXT NOT NULL,
    FOREIGN KEY (intern_id)
        REFERENCES interns(intern_id)
)
""")

# Step 5 — Insert mock applicants
applicants = [
    (1, "Ahmed Ali", "Data Science", "Cairo University", "2026-09-01", "Selected"),
    (2, "Sara Mohamed", "Data Science", "Helwan University", "2026-09-02", "Selected"),
    (3, "Omar Hassan", "Data Science", "Ain Shams University", "2026-09-03", "Rejected"),
    (4, "Mariam Adel", "Data Science", "Helwan University", "2026-09-04", "Selected"),
    (5, "Youssef Samir", "Data Science", "Cairo University", "2026-09-05", "Under Review"),
    (6, "Nour Khaled", "Web Development", "Helwan University", "2026-09-06", "Selected"),
    (7, "Amr Tarek", "Web Development", "Cairo University", "2026-09-07", "Selected"),
    (8, "Salma Mostafa", "Web Development", "Ain Shams University", "2026-09-08", "Rejected"),
    (9, "Hana Mahmoud", "Web Development", "Helwan University", "2026-09-09", "Selected"),
    (10, "Karim Wael", "Web Development", "Cairo University", "2026-09-10", "Under Review"),
    (11, "Laila Ashraf", "Artificial Intelligence", "Cairo University", "2026-09-11", "Selected"),
    (12, "Ziad Mostafa", "Artificial Intelligence", "Helwan University", "2026-09-12", "Selected"),
    (13, "Farida Hany", "Artificial Intelligence", "Ain Shams University", "2026-09-13", "Rejected"),
    (14, "Malak Ahmed", "Artificial Intelligence", "Helwan University", "2026-09-14", "Selected"),
    (15, "Seif Mahmoud", "Artificial Intelligence", "Cairo University", "2026-09-15", "Under Review"),
    (16, "Nada Ehab", "Cyber Security", "Helwan University", "2026-09-16", "Selected"),
    (17, "Adam Fathy", "Cyber Security", "Cairo University", "2026-09-17", "Selected"),
    (18, "Mina George", "Cyber Security", "Ain Shams University", "2026-09-18", "Rejected"),
    (19, "Rana Emad", "Cyber Security", "Helwan University", "2026-09-19", "Selected"),
    (20, "Peter Nabil", "Cyber Security", "Cairo University", "2026-09-20", "Under Review")
]

cursor.executemany("""
INSERT OR IGNORE INTO applicants
VALUES (?, ?, ?, ?, ?, ?)
""", applicants)

# Step 6 — Insert mock interns
interns = [
    (1, 1, "Data Science", "2026-09-28", "Completed"),
    (2, 2, "Data Science", "2026-09-28", "Completed"),
    (3, 4, "Data Science", "2026-09-28", "Dropped Out"),
    (4, 6, "Web Development", "2026-09-28", "Completed"),
    (5, 7, "Web Development", "2026-09-28", "Completed"),
    (6, 9, "Web Development", "2026-09-28", "Dropped Out"),
    (7, 11, "Artificial Intelligence", "2026-09-28", "Completed"),
    (8, 12, "Artificial Intelligence", "2026-09-28", "Completed"),
    (9, 14, "Artificial Intelligence", "2026-09-28", "Completed"),
    (10, 16, "Cyber Security", "2026-09-28", "Completed"),
    (11, 17, "Cyber Security", "2026-09-28", "Dropped Out"),
    (12, 19, "Cyber Security", "2026-09-28", "Completed")
]

cursor.executemany("""
INSERT OR IGNORE INTO interns
VALUES (?, ?, ?, ?, ?)
""", interns)

# Step 7 — Insert mock hackathon scores
scores = [
    (1, 92, "Data Science"),
    (2, 87, "Data Science"),
    (4, 78, "Web Development"),
    (5, 95, "Web Development"),
    (7, 89, "Artificial Intelligence"),
    (8, 96, "Artificial Intelligence"),
    (9, 82, "Artificial Intelligence"),
    (10, 91, "Cyber Security"),
    (12, 85, "Cyber Security")
]

cursor.executemany("""
INSERT OR IGNORE INTO hackathon_scores
VALUES (?, ?, ?)
""", scores)

# Step 8 — Save changes
conn.commit()
conn.close()

print("Database created successfully!")
print("Tables: applicants, interns, hackathon_scores")
