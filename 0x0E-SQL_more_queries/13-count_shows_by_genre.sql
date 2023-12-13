/* A script */
-- task 14
SELECT g.name AS genre, COUNT(*) AS number_of_shows
	FROM tv_show_genres as g
		JOIN tv_shows as s
		ON g.genre_id = s.id
	GROUP BY name
	ORDER BY number_of_shows DESC;
