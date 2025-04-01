SELECT 
    PARKINSON_DIAGNOSIS,
    AVG(UPDRS) AS avg_updrs,
    AVG(MOCA) AS avg_moca
FROM TEST1.STREAM.TEST1_FEATUREENG
GROUP BY PARKINSON_DIAGNOSIS
ORDER BY PARKINSON_DIAGNOSIS;