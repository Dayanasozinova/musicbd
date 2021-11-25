import sqlalchemy


engine = sqlalchemy.create_engine('postgresql://artur:qwerty@localhost:5432/music')
engine
connection = engine.connect()
connection
#------------------------------------------------------------------------------
connection.execute("""SELECT album_name, yars_of_issue FROM albums
    WHERE yars_of_issue = 2018
;""").fetchall()
#------------------------------------------------------------------------------
max_duration = connection.execute("""
SELECT max(duration)
FROM track;""").fetchall()
connection.execute(f"""SELECT track_name, duration FROM track
    WHERE duration = {max_duration[0][0]};""").fetchall()
#------------------------------------------------------------------------------
connection.execute("""SELECT track_name FROM track
    WHERE duration > 210;""").fetchall()
#------------------------------------------------------------------------------
connection.execute("""SELECT collection_name FROM collection   
    WHERE yars_of_issue BETWEEN 2018 AND 2020;""").fetchall()
#------------------------------------------------------------------------------
collection_name = connection.execute("""SELECT collection_name FROM collection
    ;""").fetchall()

name_list = []
for name in collection_name:
    if len(name) == 1:
        name_list.append(name)
print(name_list)
#------------------------------------------------------------------------------
connection.execute("""SELECT track_name FROM track    
    WHERE track_name LIKE '%%My%%' OR track_name LIKE '%%Мой%%';""").fetchall()









# connection.execute("""INSERT INTO track_collection (id, collection, track)    
#            VALUES (17, 1, 9),
# 		(18, 2, 10),
# 		(19, 3, 11),
# 		(20, 4, 12),
#         (21, 5, 13),
#         (22, 6, 14),
#         (23, 7, 15);

# """)


