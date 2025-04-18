--categorizing BMI
CREATE OR REPLACE TABLE TEST1.STREAM.TEST1_TRANSFORMED AS
SELECT 
  *,
  CASE
    WHEN BMI < 18.5 THEN 'Underweight'
    WHEN BMI BETWEEN 18.5 AND 24.9 THEN 'Normal'
    WHEN BMI BETWEEN 25 AND 29.9 THEN 'Overweight'
    ELSE 'Obese'
  END AS BMI_CATEGORY,

--risk score 0/1 
  (HYPERTENSION + DIABETES + STROKE + DEPRESSION + FAMILYHISTORYPARKINSONS) AS RISK_SCORE

FROM TEST1.STREAM.TEST1_CLEANED;