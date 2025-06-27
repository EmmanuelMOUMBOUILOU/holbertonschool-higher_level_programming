-- File: SQL_more_queries/9-cities_by_state_join.sql
SELECT cities.id, cities.name, states.name
FROM cities, states
WHERE cities.state_id = states.id
ORDER BY cities.id;
