/* A script that uses the hbtn_0d_tvshows databases to lists all genres
of the show `Dexter` */
-- task 15
SELECT g.name
	FROM tv_shows AS s
		JOIN tv_show_genres AS sg
		ON s.id = sg.show_id
		JOIN tv_genres AS g
		ON sg.genre_id = g.id
	WHERE s.title = 'Dexter'
	ORDER BY g.name;
