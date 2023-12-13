/* A script that uses the databases to lists all genres of the show `Dexter` */
-- task 15
SELECT g.name
FROM tv_genres AS g
JOIN tv_show_genres AS sg ON g.id = sg.genre_id
JOIN tv_shows AS s ON sg.show_id = s.id
WHERE s.title = 'Dexter'
ORDER BY g.name;
