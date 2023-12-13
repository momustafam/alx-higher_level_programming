/* A script that uses the hbtn_0d_tvshows databases to list all genres 
not linked to the show `Dexter` */
-- task 18
SELECT name
	FROM tv_genres
    	WHERE tv_genres.id NOT IN (
		SELECT tv_genres.id FROM tv_genres
		JOIN tv_show_genres ON tv_genres.id=tv_show_genres.genre_id
		JOIN tv_shows ON tv_shows.id=tv_show_genres.show_id
		WHERE tv_shows.title = "DEXTER" 
	)
   ORDER BY name;
