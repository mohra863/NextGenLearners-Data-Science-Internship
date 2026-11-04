# NextGenLearners — SQL & Data Analysis Dashboard

## Project Overview

This project was developed as part of the NextGenLearners Data Science Internship.

The project focuses on database creation, SQL querying, data analysis, and interactive dashboard development using Python and Streamlit.

Since no dataset was provided, a synthetic dataset was created to simulate an internship application and performance tracking system.

## Dataset

The SQLite database contains three tables:

| Table | Description |
|---|---|
| `applicants` | Contains applicant information and application status. |
| `interns` | Contains internship participants and their completion status. |
| `hackathon_scores` | Contains hackathon scores for interns. |

The dataset includes four domains:

- Artificial Intelligence
- Data Science
- Cyber Security
- Web Development

## SQL Analysis

Five SQL queries were developed to analyze the database:

1. **Completed Interns per Domain** — Counts completed interns in each domain.
2. **Average Hackathon Score per Domain** — Calculates the average score for each domain.
3. **Top Performers** — Identifies interns who scored 85 or above.
4. **Conversion Rate per Domain** — Calculates the percentage of applicants who completed the internship.
5. **Completion vs. Dropout Analysis** — Compares completed interns and dropouts across domains.

The queries demonstrate the use of:

- `SELECT`, `WHERE`, and `ORDER BY`
- `GROUP BY` and aggregate functions
- `JOIN` and `LEFT JOIN`
- `COUNT()`, `AVG()`, and `ROUND()`

## Interactive Dashboard

The dashboard was developed using Streamlit and includes:

- **Program Funnel:** Total applicants and completed interns.
- **Completion Rate:** Bar chart showing completion rates by domain.
- **Average Hackathon Score:** Bar chart comparing average scores.
- **Top 10 Performers:** Leaderboard sorted by hackathon score.
- **Intern Distribution:** Pie chart showing the distribution of interns across domains.
- **Domain Filter:** Interactive dropdown to filter dashboard results by domain.

The pie chart displays the overall distribution across all domains, independently of the selected filter.

## Technologies Used

- Python 3.12.3
- SQLite
- SQL
- Pandas
- Streamlit
- Plotly
- Jupyter Notebook

## Project Structure

```text
week3-sql-dashboard/
│
├── create_database.py
├── nextgen.db
├── Week3_SQL_Queries.ipynb
├── dashboard.py
├── requirements.txt
├── README.md
└── demo.mp4
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone <YOUR_REPOSITORY_URL>
cd week3-sql-dashboard
```

### 2. Create a virtual environment

```bash
python3.12 -m venv .venv
```

### 3. Activate the environment

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

## Running the Dashboard

Make sure you are inside the project directory and the virtual environment is activated.

Run:

```bash
streamlit run dashboard.py
```

The dashboard will open in your browser.

## Demo

A demo video is included to demonstrate the dashboard, domain filtering, charts, and leaderboard.

## Learning Outcomes

Through this project, I practiced:

- Creating and managing SQLite databases.
- Writing SQL queries for data analysis.
- Understanding relationships between database tables.
- Calculating performance metrics.
- Building interactive dashboards using Streamlit.
- Visualizing data using Plotly and Streamlit charts.

---

**Developed as part of the NextGenLearners Data Science Internship.**