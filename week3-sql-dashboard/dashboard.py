
import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px

# Step 4 — Load data and create the dashboard filter

st.set_page_config(
    page_title="NextGenLearners Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 NextGenLearners Program Performance Dashboard")

# Connect to the SQLite database
conn = sqlite3.connect("nextgen.db")

# Load the three tables
applicants = pd.read_sql("SELECT * FROM applicants;", conn)
interns = pd.read_sql("SELECT * FROM interns;", conn)
scores = pd.read_sql("SELECT * FROM hackathon_scores;", conn)

conn.close()

# Create the domain filter
domain_list = ["All"] + sorted(applicants["domain"].unique().tolist())

selected_domain = st.selectbox(
    "Filter by Domain",
    domain_list
)

# Filter data based on the selected domain

if selected_domain == "All":
    applicants_filtered = applicants.copy()
    interns_filtered = interns.copy()
else:
    applicants_filtered = applicants[
        applicants["domain"] == selected_domain
    ]

    interns_filtered = interns[
        interns["domain"] == selected_domain
    ]

# Count completed interns only
completed_interns = interns_filtered[
    interns_filtered["completion_status"] == "Completed"
]

# Display the funnel metrics
st.subheader("Program Funnel")

col1, col2 = st.columns(2)

with col1:
    st.metric(
        label="Total Applicants",
        value=len(applicants_filtered)
    )

with col2:
    st.metric(
        label="Total Completed Interns",
        value=len(completed_interns)
    )

# Calculate completion rate per domain

completed_applicant_ids = interns[
    interns["completion_status"] == "Completed"
][["applicant_id"]].drop_duplicates()

applicants_with_completion = applicants.merge(
    completed_applicant_ids.assign(completed=1),
    on="applicant_id",
    how="left"
)

applicants_with_completion["completed"] = (
    applicants_with_completion["completed"].fillna(0)
)

completion_rate = (
    applicants_with_completion
    .groupby("domain")
    .agg(
        total_applicants=("applicant_id", "nunique"),
        total_completed=("completed", "sum")
    )
    .reset_index()
)

completion_rate["completion_rate_pct"] = (
    100 * completion_rate["total_completed"]
    / completion_rate["total_applicants"]
)

# Apply the selected domain filter

if selected_domain != "All":
    completion_rate = completion_rate[
        completion_rate["domain"] == selected_domain
    ]

# Display the completion rate chart

st.subheader("Completion Rate per Domain")

st.bar_chart(
    completion_rate.set_index("domain")["completion_rate_pct"],
    y_label="Completion Rate (%)"
)

# Calculate average hackathon score per domain

average_scores = (
    scores.groupby("domain")
    .agg(avg_score=("score", "mean"))
    .reset_index()
)

average_scores["avg_score"] = average_scores["avg_score"].round(2)

# Apply the selected domain filter

if selected_domain != "All":
    average_scores = average_scores[
        average_scores["domain"] == selected_domain
    ]

# Display the average hackathon score chart

st.subheader("Average Hackathon Score per Domain")

st.bar_chart(
    average_scores.set_index("domain")["avg_score"],
    y_label="Average Score"
)

# Create the leaderboard of top performers

leaderboard = scores.merge(
    interns[["intern_id", "completion_status"]],
    on="intern_id",
    how="left"
)

leaderboard = leaderboard.sort_values(
    by="score",
    ascending=False
)

# Apply the selected domain filter

if selected_domain != "All":
    leaderboard = leaderboard[
        leaderboard["domain"] == selected_domain
    ]

# Display the top 10 performers

st.subheader("Top 10 Hackathon Performers")

leaderboard = leaderboard.head(10)

st.dataframe(
    leaderboard,
    use_container_width=True,
    hide_index=True
)

# Pie Chart — Intern Distribution by Domain

st.subheader("Intern Distribution by Domain")

# Count interns in each domain
intern_distribution = (
    interns.groupby("domain")
    .agg(intern_count=("intern_id", "nunique"))
    .reset_index()
)

# Create the pie chart using all domains
fig = px.pie(
    intern_distribution,
    names="domain",
    values="intern_count",
    title="Interns Distribution",
    hole=0.4
)

# Display the chart
st.plotly_chart(fig, use_container_width=True)



