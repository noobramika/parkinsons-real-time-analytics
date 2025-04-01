SELECT 
    BMI_CATEGORY,
    PARKINSON_DIAGNOSIS,
    COUNT(*) AS patient_count
FROM TEST1.STREAM.TEST1_FEATUREENG
GROUP BY BMI_CATEGORY, PARKINSON_DIAGNOSIS
ORDER BY BMI_CATEGORY, PARKINSON_DIAGNOSIS;