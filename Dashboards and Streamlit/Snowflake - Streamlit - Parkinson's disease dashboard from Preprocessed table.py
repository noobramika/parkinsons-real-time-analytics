# Import packages
import streamlit as st
import pandas as pd
from snowflake.snowpark.context import get_active_session

# Get the current session
session = get_active_session()

st.title("Parkinson’s Disease Dashboard")
st.markdown("This dashboard provides visual insights from the Parkinson’s dataset using Snowflake and Streamlit.")


# Query 1: Diagnosis Count by Gender and Education
query1 = """
SELECT 
    GENDER_LABEL,
    EDUCATION_LABEL,
    COUNT(*) AS diagnosis_count
FROM TEST1.STREAM.TEST1_FEATUREENG
WHERE DIAGNOSIS = 1
GROUP BY GENDER_LABEL, EDUCATION_LABEL
ORDER BY GENDER_LABEL, EDUCATION_LABEL;
"""
df1 = session.sql(query1).to_pandas()
pivot1 = df1.pivot(index="GENDER_LABEL", columns="EDUCATION_LABEL", values="DIAGNOSIS_COUNT")

st.subheader("Diagnosis Count by Gender and Education")
st.dataframe(pivot1)
st.bar_chart(pivot1)


# Query 2: Diagnosis Count by BMI Category and Gender
query2 = """
SELECT 
    BMI_CATEGORY,
    GENDER_LABEL,
    COUNT(*) AS diagnosis_count
FROM TEST1.STREAM.TEST1_FEATUREENG
WHERE DIAGNOSIS = 1
GROUP BY BMI_CATEGORY, GENDER_LABEL
ORDER BY BMI_CATEGORY, GENDER_LABEL;
"""
df2 = session.sql(query2).to_pandas()
pivot2 = df2.pivot(index="BMI_CATEGORY", columns="GENDER_LABEL", values="DIAGNOSIS_COUNT")

st.subheader("Diagnosis Count by BMI Category and Gender")
st.bar_chart(pivot2)


# Query 3: Average UPDRS and MOCA Scores by Diagnosis
query3 = """
SELECT 
    PARKINSON_DIAGNOSIS,
    AVG(UPDRS) AS avg_updrs,
    AVG(MOCA) AS avg_moca
FROM TEST1.STREAM.TEST1_FEATUREENG
GROUP BY PARKINSON_DIAGNOSIS
ORDER BY PARKINSON_DIAGNOSIS;
"""
df3 = session.sql(query3).to_pandas()
st.subheader("Average UPDRS and MOCA Scores by Diagnosis")
st.bar_chart(data=df3.set_index("PARKINSON_DIAGNOSIS")[["AVG_UPDRS", "AVG_MOCA"]])


# Query 4: BMI Category vs Diagnosis
query4 = """
SELECT 
    BMI_CATEGORY,
    PARKINSON_DIAGNOSIS,
    COUNT(*) AS patient_count
FROM TEST1.STREAM.TEST1_FEATUREENG
GROUP BY BMI_CATEGORY, PARKINSON_DIAGNOSIS
ORDER BY BMI_CATEGORY, PARKINSON_DIAGNOSIS;
"""
df4 = session.sql(query4).to_pandas()
pivot4 = df4.pivot(index="BMI_CATEGORY", columns="PARKINSON_DIAGNOSIS", values="PATIENT_COUNT")

st.subheader("BMI Category vs Diagnosis")
st.bar_chart(pivot4)


# Query 6: Risk Score vs Diagnosis
query6 = """
SELECT 
    RISK_SCORE,
    PARKINSON_DIAGNOSIS,
    COUNT(*) AS patient_count
FROM TEST1.STREAM.TEST1_FEATUREENG
GROUP BY RISK_SCORE, PARKINSON_DIAGNOSIS
ORDER BY RISK_SCORE, PARKINSON_DIAGNOSIS;
"""
df6 = session.sql(query6).to_pandas()
pivot6 = df6.pivot(index="RISK_SCORE", columns="PARKINSON_DIAGNOSIS", values="PATIENT_COUNT")

st.subheader("Risk Score vs Diagnosis")
st.bar_chart(pivot6)