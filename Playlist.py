"""Class for the playlist"""

from typing import List
from Song import Song


class Playlist:
    """Playlists"""

    def __init__(self, title: str, songs: List[Song] = []) -> None:
        self.ID: int
        self.title: str = title
        self.songs: list = songs

    @property
    def get_title(self) -> str:
        return f"{self.title}"
    
    # playlist set ID()

    def add_song(self, song: Song) -> None:
        self.songs.append(song)

    @property
    def get_songs(self) -> list:
        return self.songs

    def __repr__(self) -> str:
        return f"Playlist : {self.title}, with {len(self.songs)} songs"
