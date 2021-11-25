import sqlalchemy

engine = sqlalchemy.create_engine('postgresql://artur:qwerty@localhost:5432/music')
engine
connection = engine.connect()
connection


connection.execute("""INSERT INTO album_singer (id, album, singer)    
           VALUES (1, 1, 8),
                  (2, 2, 7),
                  (3, 3, 6),
                  (4, 4, 5),
                  (5, 5, 4),
                  (6, 6, 3),
                  (7, 7, 2),
                  (8, 8, 1);
""")
#----------------------------------------------------------------------
connection.execute("""INSERT INTO album (id, akbum_name, yars_of_issue)    
           VALUES (1, 'Spring', 1987),
                  (2, 'Five', 2019),
                  (3, 'Jazz', 2007),
                  (4, 'The little boy', 2017),
                  (5, 'My spirit', 2000),
                  (6, 'Беспечный ангел', 2001),
                  (7, 'Every Kingdom', 2006),
                  (8, 'Замок саратау', 2018);
""")
#----------------------------------------------------------------------
connection.execute("""INSERT INTO collection (id, collection_name, yars_of_issue)    
           VALUES (1, 'Gold', 2019),
                  (2, 'silver', 2018),
                  (3, 'The best', 2000),
                  (4, 'For spring day', 2021),
                  (5, 'Together', 2018),
                  (6, 'Today', 2019),
                  (7, 'For monday', 2005),
                  (8, 'Gold edition', 2020);
""")
#-----------------------------------------------------------------------
connection.execute("""INSERT INTO collection (id, genre_name)    
           VALUES (1, 'Pop'),
                  (2, 'Hip-hop'),
                  (3, 'Rep'),
                  (4, 'Jazz'),
                  (5, 'Rock');
""")
#-------------------------------------------------------------------------
connection.execute("""INSERT INTO genre_singer (id, genre, singer)    
           VALUES (1, 1, 1),
                  (2, 2, 1),
                  (3, 5, 5),
                  (4, 4, 4),
                  (5, 4, 2),
                  (6, 3, 3),
                  (7, 2, 8),
                  (8, 3, 7),
                  (9, 2, 6);
""")
#--------------------------------------------------------------------------
connection.execute("""INSERT INTO singers (id, singer_name)    
           VALUES (1, 'Alla Pugacheva'),
                  (2, 'Sia'),
                  (3, 'James Brown'),
                  (4, 'Troye Sivan'),
                  (5, 'Ben Howard'),
                  (6, 'Ariya'),
                  (7, 'Swan Mortuus'),
                  (8, 'GUF');
""")
#-------------------------------------------------------------------------
connection.execute("""INSERT INTO track (id, track_name, album, duration)    
           VALUES (1, 'Улица роз', 6, 653),
                  (2, 'Woolwes', 7, 150),
                  (3, 'Саратау', 8, 265),
                  (4, 'Boy Boy', 4, 569),
                  (5, 'Three', 3, 352),
                  (6, 'Fire', 5, 145),
                  (7, 'My Love', 1, 265),
                  (8, 'Issues', 2, 254),
                  (9, 'Donda', 2, 486),
                  (10, 'Dayana', 8, 365),
                  (11, 'Man', 7, 756),
                  (12, 'Мой милый', 5, 456),
                  (13, 'Moon', 8, 159),
                  (14, 'Dog', 1, 358),
                  (15, '-', 6, 753);
""")
#-------------------------------------------------------------------------------
connection.execute("""INSERT INTO track_collection (id, collection, track)    
           VALUES (1, 1, 8),
                  (2, 2, 7),
                  (3, 3, 6),
                  (4, 4, 5),
                  (5, 5, 4),
                  (6, 6, 3),
                  (7, 7, 2),
                  (8, 8, 1),
                  (9, 8, 8),
                  (10, 7, 7),
                  (11, 6, 6),
                  (12, 5, 5),
                  (13, 4, 4),
                  (14, 3, 3),
                  (15, 2, 2),
                  (16, 1, 1),
                  (17, 1, 9),
                  (18, 2, 10),
                  (19, 3, 11),
                  (20, 4, 12),
                  (21, 5, 13),
                  (22, 6, 14),
                  (23, 7, 15);
""")