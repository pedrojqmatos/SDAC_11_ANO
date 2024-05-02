CREATE TABLE 'Artist' ('id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,'name' TEXT);
CREATE TABLE 'Genre' ('id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,'name' TEXT);
CREATE TABLE 'Album' ('id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,'artist_id' INTEGER, 'title' TEXT);
CREATE TABLE 'Track' ('id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, 'title' TEXT, 'album_id' INTEGER, 'genre_id' INTEGER, 'len' INTEGER, 'rating' INTEGER, 'count' INTEGER);
INSERT INTO Artist (name) VALUES ('AC/DC')
INSERT INTO Artist (name) VALUES ('America')
INSERT INTO Artist (name) VALUES ('Megadeth')
INSERT INTO Artist (name) VALUES ('Katy Perry')
INSERT INTO Genre (name) VALUES ('Rock')
INSERT INTO Genre (name) VALUES ('Easy Listening')
INSERT INTO Genre (name) VALUES ('Metal')
INSERT INTO Genre (name) VALUES ('Pop')
INSERT INTO Album (artist_id, title) VALUES ( 1, 'WHO MADE WHO')
INSERT INTO Album (artist_id, title) VALUES ( 2, 'Greatest Hits')
INSERT INTO Album (artist_id, title) VALUES ( 3, 'Metal Forever')
INSERT INTO Album (artist_id, title) VALUES ( 4, 'FantasticBeasts')
INSERT INTO Track (title, album_id, genre_id, len, rating, count) VALUES ('Hells Bells', 1, 1, 513, 5, 61)
INSERT INTO Track (title, album_id, genre_id, len, rating, count) VALUES ('Shake Your Foundations', 1, 1, 354, 5, 70)
INSERT INTO Track (title, album_id, genre_id, len, rating, count) VALUES ('Chase the Ace', 1, 1, 301, 5, 56);
INSERT INTO Track (title, album_id, genre_id, len, rating, count) VALUES ('For Those About to Rock We Salute You', 1, 1, 554, 5, 31);
INSERT INTO Track (title, album_id, genre_id, len, rating, count) VALUES ('Rode Across the Desert', 2, 2, 410, 3, 23);
INSERT INTO Track (title, album_id, genre_id, len, rating, count) VALUES ('Now You Are Gone', 2, 2, 330, 3, 12);
INSERT INTO Track (title, album_id, genre_id, len, rating, count) VALUES ('Tin Man', 2, 2, 233, 3, 46);
INSERT INTO Track (title, album_id, genre_id, len, rating, count) VALUES ('Sister Golden Air', 2, 2, 228, 3, 33);
INSERT INTO Track (title, album_id, genre_id, len, rating, count) VALUES ('Dystopia', 3, 3, 334, 4, 78);
INSERT INTO Track (title, album_id, genre_id, len, rating, count) VALUES ('Symphony od Destruction', 3 , 3, 432, 4, 89);
INSERT INTO Track (title, album_id, genre_id, len, rating, count) VALUES ('Tornado of Souls', 3, 3, 645, 4, 54);
INSERT INTO Track (title, album_id, genre_id, len, rating, count) VALUES ('A Toute Le Monde', 3, 3, 543, 4, 37);
INSERT INTO Track (title, album_id, genre_id, len, rating, count) VALUES ('I Kissed a Girl', 4, 4, 233, 3, 45);
INSERT INTO Track (title, album_id, genre_id, len, rating, count) VALUES ('Dark Horse', 4, 4, 256, 3, 65);
INSERT INTO Track (title, album_id, genre_id, len, rating, count) VALUES ('Hot N Cold', 4, 4, 345, 3, 33);
INSERT INTO Track (title, album_id, genre_id, len, rating, count) VALUES ('Last Friday', 4, 4, 476, 3, 28);
SELECT Album.title, Artist.name FROM Album JOIN Artist ON Album.artist_id = artist_id
SELECT Album.title, Album.artist_id, Artist.id , Artist.name FROM Album JOIN Artist ON Album.artist_id = Album.id
SELECT Track.title, Track.genre_id, Genre.id, Genre.name FROM Track JOIN Genre
SELECT Track.title, Genre.name FROM Track JOIN Genre on Track.genre_id = Genre.id
SELECT Track.title, Artist.name, Album.title, Genre.name FROM Track JOIN Genre JOIN Album JOIN Artist on Track.genre_id = Genre.id AND Track.album_id = Album.id and Album.artist_id = Artist.id




CREATE TABLE 'User' ('id' INTEGER PRIMARY KEY, 'name' TEXT UNIQUE, 'email' TEXT);
CREATE TABLE 'Course' ('id' INTEGER PRIMARY KEY, 'title' TEXT UNIQUE);
CREATE TABLE 'Member' ('user_id' INTEGER, 'course_id' INTEGER, 'role' INTEGER, PRIMARY KEY (user_id, course_id));
INSERT INTO User (name, email) VALUES ('Jane', 'jane@tsugi.org');
INSERT INTO User (name, email) VALUES ('Ed', 'ed@tsugi.org');
INSERT INTO User (name, email) VALUES ('Sue', 'sue@tsugi.org');
INSERT INTO Course (title) VALUES ('Python');
INSERT INTO Course (title) VALUES ('SQL');
INSERT INTO Course (title) VALUES ('PHP');
INSERT INTO Member (user_id, course_id, role) VALUES (1, 1, 1);
INSERT INTO Member (user_id, course_id, role) VALUES (2, 1, 0);
INSERT INTO Member (user_id, course_id, role) VALUES (3, 1, 0);
INSERT INTO Member (user_id, course_id, role) VALUES (1, 2, 0);
INSERT INTO Member (user_id, course_id, role) VALUES (2, 2, 1);
INSERT INTO Member (user_id, course_id, role) VALUES (2, 3, 1);
INSERT INTO Member (user_id, course_id, role) VALUES (3, 3, 0);
