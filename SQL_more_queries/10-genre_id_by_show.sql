-- yes
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
INNER JOIN tv_show_genres ON cities.id = tv_show_genres.genre_id
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
