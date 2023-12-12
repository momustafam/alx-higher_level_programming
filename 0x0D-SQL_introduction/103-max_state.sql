-- task 21
-- get max temperature for each state ordered by state name
SELECT state, MAX(value) as max_temp
	FROM temperatures
	GROUP BY state
	ORDER BY state;
