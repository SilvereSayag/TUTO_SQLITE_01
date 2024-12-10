import sqlite3
from Song import Song
from Playlist import Playlist

def connect_to_dB():
    conn = sqlite3.connect("PlayList.db")
    return conn

# TO DO NOW
def add_song_to_playlist(playlist : Playlist, song : Song) -> None:
    return

def insert_song(song: Song, conn, cursor) -> None:

    with conn:
        cursor.execute(
            """INSERT INTO songs VALUES (:ID, :title, :band_name, :votes)""",
            {
                "ID": None,
                "title": song.title,
                "band_name": song.band_name,
                "votes": song.votes,
            },
        )
    cursor.execute("SELECT max(ID) FROM songs")
    t = cursor.fetchone()
    song.set_ID(t[0])


def get_song_by_ID(ID: int, cursor):

    cursor.execute("SELECT * FROM songs where ID = :ID", {"ID": ID})
    t = cursor.fetchall()
    return t


def get_song_by_title(title: str, cursor):

    cursor.execute("SELECT * FROM songs where title = :title", {"title": title})
    t = cursor.fetchall()
    print(f"inside func : {t}")
    return t


def update_song_vote(song: Song, votes: int, conn, cursor) -> None:
    with conn:
        cursor.execute(
            """UPDATE songs SET votes = :votes
               WHERE title = :title AND bandName = :band_name """,
            {"title": song.title, "band_name": song.band_name, "votes": votes},
        )


def remove_song(song: Song, conn, cursor):
    with conn:
        cursor.execute(
            "DELETE from songs WHERE title = :title AND bandName = :band_name",
            {"title": song.title, "band_name": song.band_name},
        )


def print_songs(cursor):

    cursor.execute("SELECT * FROM songs")
    print(f"{cursor.fetchall()}")


def create_tables(conn, cursor):
    with conn:
        cursor.execute("DROP TABLE IF EXISTS songs;")
        cursor.execute("DROP TABLE IF EXISTS playlists;")
        cursor.execute("DROP TABLE IF EXISTS playlists_songs;")

        cursor.execute(
            """
            CREATE TABLE songs(
                ID INTEGER PRIMARY KEY, 
                title TEXT NOT NULL,
                bandName TEXT,
                votes INTEGER 
            )
        """
        )

        cursor.execute(
            """
            CREATE TABLE playlists(
                ID INTEGER PRIMARY KEY, 
                title TEXT
            )
        """
        )

        cursor.execute(
            """
            CREATE TABLE playlists_songs (
                song_id INTEGER,
                playlist_id INTEGER,
                PRIMARY KEY (song_id, playlist_id)
                FOREIGN KEY (song_id)
                    REFERENCES songs (id)
                        ON DELETE CASCADE
                        ON UPDATE NO ACTION,
                FOREIGN KEY (playlist_id)
                    REFERENCES playlists (id)
                        ON DELETE CASCADE
                        ON UPDATE NO ACTION      
            );
        """
        )


