/* A script that lists all cities contained in the database hbtn_0d_usa. */
-- the query
SELECT cities.id, cities.name, states.names
	FROM cities, states
	ORDER BY cities.id;
