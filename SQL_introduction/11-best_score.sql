-- File: SQL_introduction/11-best_score.sql
SELECT score, name FROM second_table
WHERE score >= 10
ORDER BY score DESC;