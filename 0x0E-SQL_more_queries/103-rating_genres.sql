-- task 20 (get the sum of rates of each show)
SELECT genre.name, SUM(rates.rate) AS rating
	FROM tv_genres AS genre
		LEFT JOIN tv_show_genres AS sho_gen
		ON genre.id = sho_gen.genre_id
		LEFT JOIN tv_show_ratings AS rates
		ON sho_gen.show_id = rates.show_id
	GROUP BY genre.name
	ORDER BY rating DESC;
