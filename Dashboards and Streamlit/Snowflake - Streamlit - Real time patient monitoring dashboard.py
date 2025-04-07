# Import necessary packages
import streamlit as st
import pandas as pd
from snowflake.snowpark.context import get_active_session

# Get Snowflake session
session = get_active_session()

# Title
st.title("Real-Time Patient Monitoring Dashboard")
st.markdown("This dashboard displays live updates from the raw Parkinson’s dataset. Re-run the app after pipeline ingestion to reflect updates.")

# Query 1: Total number of patients
query_count = "SELECT COUNT(*) AS total_patients FROM TEST1.STREAM.TEST1"
df_count = session.sql(query_count).to_pandas()
st.metric("Total Patients", df_count['TOTAL_PATIENTS'][0])

# Query 2: Latest 10 records (based on PATIENTID)
query_latest = """
SELECT * 
FROM TEST1.STREAM.TEST1 
ORDER BY PATIENTID DESC 
LIMIT 10
"""
df_latest = session.sql(query_latest).to_pandas()
st.subheader("Latest 10 Patient Records")
st.dataframe(df_latest, use_container_width=True)

# Query 3: Diagnosis distribution
query_diag = """
SELECT 
    DIAGNOSIS,
    COUNT(*) AS count
FROM TEST1.STREAM.TEST1
GROUP BY DIAGNOSIS
ORDER BY DIAGNOSIS
"""
df_diag = session.sql(query_diag).to_pandas()
df_diag['DIAGNOSIS'] = df_diag['DIAGNOSIS'].replace({0: "No", 1: "Yes"})
df_diag.set_index('DIAGNOSIS', inplace=True)

st.subheader("Diagnosis Distribution (Live)")
st.bar_chart(df_diag)

# Query 4: Gender distribution
query_gender = """
SELECT 
    CASE 
        WHEN GENDER = 0 THEN 'Male'
        WHEN GENDER = 1 THEN 'Female'
        ELSE 'Unknown'
    END AS gender,
    COUNT(*) AS count
FROM TEST1.STREAM.TEST1
GROUP BY gender
ORDER BY gender
"""
df_gender = session.sql(query_gender).to_pandas()
df_gender.set_index('GENDER', inplace=True)

st.subheader("Gender Distribution (Live)")
st.bar_chart(df_gender)