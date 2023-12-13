/* A script that lists all `Comedy` shows in the database hbtn_0d_tvshows */
-- task 16
SELECT s.title
    FROM tv_genres AS g
            JOIN tv_show_genres AS sg
            ON g.id = sg.genre_id
            JOIN tv_shows AS s
            ON sg.show_id = s.id
    WHERE g.name = 'Comedy'
    ORDER BY s.title;
