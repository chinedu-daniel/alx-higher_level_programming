-- Script: Lists all the cities of California that are in the database

SELECT * 
FROM cities
WHERE state_id = (
	SELECT id 
	FROM states
	WHERE name = 'California'
)
ORDER BY id ASC;
