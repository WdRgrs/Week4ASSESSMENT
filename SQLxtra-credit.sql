-- ARTIST TABLE
SELECT * FROM artist
ORDER BY name DESC
LIMIT 10;



SELECT * FROM artist
WHERE name ILIKE 'black%'



SELECT * FROM artist
WHERE name ILIKE '%black%';



-- EMPLOYEE TABLE
SELECT * FROM employee
ORDER BY birth_date DESC
LIMIT 1;



SELECT * FROM employee
ORDER BY birth_date ASC
LIMIT 1;



-- INVOICE TABLE
SELECT COUNT(*) FROM invoice
WHERE billing_state IN ('TX', 'CA', 'AZ');



SELECT AVG(total) FROM invoice;



-- MORE JOIN QUERIES
SELECT * FROM playlist_track
WHERE playlist_id IN (
  SELECT playlist_id FROM playlist WHERE name ILIKE 'music'
);
-- OR
SELECT track_id FROM playlist_track
JOIN playlist ON playlist.playlist_id = playlist_track.playlist_id
WHERE playlist.name ILIKE 'MUSIC';



SELECT name FROM track
JOIN playlist_track ON playlist_track.track_id = track.track_id
WHERE playlist_id = 5;



SELECT track.name "Track Name", playlist.name "Playlist Name" FROM track
JOIN playlist_track ON playlist_track.track_id = track.track_id
JOIN playlist ON playlist.playlist_id = playlist_track.playlist_id;



SELECT track.name "Track Name", title "Album Title" FROM track
JOIN album ON track.album_id = album.album_id
JOIN genre ON genre.genre_id = track.genre_id
WHERE genre.name ILIKE 'alternative & punk';