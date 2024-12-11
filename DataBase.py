import sqlite3
from Song import Song
from Playlist import Playlist

# Should make it a Singleton ..


class DataBase:

    def __init__(self) -> None:
        self.conn = sqlite3.connect("PlayList.db")
        self.cursor = self.conn.cursor()

    def connect_to_dB(self) -> None:

        # self.conn = sqlite3.connect(":memory:")
        self.conn = sqlite3.connect("PlayList.db")
        self.cursor = self.conn.cursor()
        return

    def add_song_from_playlist(self, playlist: Playlist) -> None:

        for song in playlist.songs:
            with self.conn:
                self.cursor.execute(
                    """INSERT INTO playlists_songs VALUES (:song_id, :playlist_id)""",
                    {"song_id": song.ID, "playlist_id": playlist.ID},
                )
        return

    def insert_playlist(self, playlist: Playlist) -> None:

        with self.conn:
            self.cursor.execute(
                """INSERT INTO playlists VALUES (:ID, :title)""",
                {"ID": None, "title": playlist.get_title},
            )
        self.cursor.execute("SELECT max(ID) FROM playlists")
        t = self.cursor.fetchone()
        playlist.ID = t[0]

    def insert_song(self, song: Song) -> None:

        with self.conn:
            self.cursor.execute(
                """INSERT INTO songs VALUES (:ID, :title, :band_name, :votes)""",
                {
                    "ID": None,
                    "title": song.title,
                    "band_name": song.band_name,
                    "votes": song.votes,
                },
            )
        self.cursor.execute("SELECT max(ID) FROM songs")
        t = self.cursor.fetchone()
        song.set_ID(t[0])

    def get_song_by_ID(self, ID: int):

        self.cursor.execute("SELECT * FROM songs where ID = :ID", {"ID": ID})
        t = self.cursor.fetchall()
        return t

    def get_song_by_title(self, title: str):

        self.cursor.execute(
            "SELECT * FROM songs where title = :title", {"title": title}
        )
        t = self.cursor.fetchall()
        print(f"inside func : {t}")
        return t

    def update_song_vote(self, song: Song, votes: int) -> None:
        with self.conn:
            self.cursor.execute(
                """UPDATE songs SET votes = :votes
                WHERE title = :title AND bandName = :band_name """,
                {"title": song.title, "band_name": song.band_name, "votes": votes},
            )

    def remove_song(self, song: Song):
        with self.conn:
            self.cursor.execute(
                "DELETE from songs WHERE title = :title AND bandName = :band_name",
                {"title": song.title, "band_name": song.band_name},
            )

    def print_songs(self):

        self.cursor.execute("SELECT * FROM songs")
        print(f"{self.cursor.fetchall()}")

    def create_tables(self):
        with self.conn:
            self.cursor.execute("DROP TABLE IF EXISTS songs;")
            self.cursor.execute("DROP TABLE IF EXISTS playlists;")
            self.cursor.execute("DROP TABLE IF EXISTS playlists_songs;")

            self.cursor.execute(
                """
                CREATE TABLE songs(
                    ID INTEGER PRIMARY KEY, 
                    title TEXT NOT NULL,
                    bandName TEXT,
                    votes INTEGER 
                )
            """
            )

            self.cursor.execute(
                """
                CREATE TABLE playlists(
                    ID INTEGER PRIMARY KEY, 
                    title TEXT
                )
            """
            )

            self.cursor.execute(
                """
                CREATE TABLE playlists_songs (
                    playlist_id INTEGER,
                    song_id INTEGER,
                    PRIMARY KEY (playlist_id, song_id)
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
