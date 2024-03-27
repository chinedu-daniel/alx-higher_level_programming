-- Script: Lists all records with score >= 10

SELECT `score`, `name`
FROM `second_table`
WHERE score >= 0
ORDER BY `score` DESC;
