SELECT 
    AGE_GROUP,
    PARKINSON_DIAGNOSIS,
    COUNT(*) AS patient_count
FROM TEST1.STREAM.test1_featureeng
GROUP BY AGE_GROUP, PARKINSON_DIAGNOSIS
ORDER BY AGE_GROUP, PARKINSON_DIAGNOSIS;