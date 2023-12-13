/* A script that lists all shows, and all genres liked to that show,
the database `hbtn_0d_tvshows`. */
-- task 17
SELECT s.title, g.name
    FROM tv_shows AS s
        LEFT JOIN tv_show_genres AS sg
        ON s.id = sg.show_id
        LEFT JOIN tv_genres AS g
        ON sg.genre_id = g.id
    ORDER BY s.title, g.name;
