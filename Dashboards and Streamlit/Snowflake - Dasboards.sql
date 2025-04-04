-- Age against Patient ID
SELECT 
    PATIENTID AS Patient_id, 
    AGE
FROM TEST1.STREAM.TEST1
ORDER BY AGE DESC;


-- Total number of patients
SELECT 
    COUNT(PATIENTID) AS total_patients
FROM TEST1.STREAM.TEST1;