import sqlalchemy


engine = sqlalchemy.create_engine('postgresql://artur:qwerty@localhost:5432/music')

connection = engine.connect()

#------------------------------1------------------------------------
connection.execute("""SELECT g.genre_name, COUNT(gs.singer) FROM genre g 
    JOIN genre_singer gs ON g.id = gs.genre
    JOIN singers s ON s.id = gs.singer
    GROUP BY g.genre_name
;""").fetchall()
#------------------------------2-----------------------------------
connection.execute("""SELECT a.album_name, COUNT(t.id) FROM albums a 
    JOIN track t ON a.id = t.album
    WHERE a.yars_of_issue >= 2019 AND a.yars_of_issue <= 2020
    GROUP BY a.album_name
;""").fetchall()
#------------------------------3------------------------------------
connection.execute("""SELECT a.album_name, AVG(duration) FROM albums a 
    JOIN track t ON a.id = t.album
    GROUP BY a.album_name
;""").fetchall()
#--------------4----при-использовании-as(album_singer)-выдает-ошибку-синтаксиса
connection.execute("""SELECT s.singer_name, a.yars_of_issue FROM singers s  
    JOIN album_singer ON s.id = album_singer.singer
    JOIN albums a ON album_singer.album = a.id
    WHERE a.yars_of_issue != 2020;
    """).fetchall()
#------------------------------5----------------------------------------
connection.execute("""SELECT c.collection_name FROM collection c  
    JOIN track_collection tc ON c.id = tc.collection
    JOIN track t ON tc.track = t.id
    JOIN albums a ON t.album = a.id
    JOIN album_singer ON a.id = album_singer.album
    JOIN singers s ON album_singer.singer = s.id
    WHERE s.singer_name = 'Ben Howard'
;
    """).fetchall()
#------------------------------6------------------------------------------
connection.execute("""SELECT a.album_name, s.singer_name, COUNT(g.genre_name) FROM albums a  
    FULL JOIN album_singer ON a.id = album_singer.album
    FULL JOIN singers s ON album_singer.singer = s.id
    FULL JOIN genre_singer gs ON s.id = gs.singer
    FULL JOIN genre g ON gs.genre = g.id
    GROUP BY s.singer_name, a.album_name
    HAVING COUNT(g.genre_name) > 1
    ;
    """).fetchall()
#-----------------------------7---------------------------------------------
connection.execute("""SELECT t.track_name FROM track t  
    FULL JOIN track_collection tc ON t.id = tc.track
    WHERE tc.track IS NULL
    ;
    """).fetchall()
#------------------------------8---------------------------------------------
connection.execute("""SELECT s.singer_name, t.track_name, t.duration FROM singers s  
    JOIN album_singer ON s.id = album_singer.singer
    JOIN albums a ON album_singer.album = a.id
    JOIN track t ON a.id = t.album
    WHERE (t.duration) = (SELECT MIN(t.duration) FROM singers s  
            JOIN album_singer ON s.id = album_singer.singer
        JOIN albums a ON album_singer.album = a.id
        JOIN track t ON a.id = t.album);
    """).fetchall()
#------------------------------9------------------------------------------------
connection.execute("""SELECT a.album_name, COUNT(t.id) FROM albums a 
    JOIN track t ON a.id = t.album
    GROUP BY a.album_name
    HAVING COUNT(t.id) = (
        SELECT MIN(cnt) FROM (
            SELECT COUNT(t.id) AS cnt from albums a
            JOIN track t ON a.id = t.album
            GROUP BY a.album_name
        )mincnt)
;""").fetchall()