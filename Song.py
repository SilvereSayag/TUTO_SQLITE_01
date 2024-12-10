"""Class for the songs use in playlist"""

class Song:
    """Songs"""

    def __init__(self, title : str, band_name : str):
        self.ID : int = -1
        self.title : str = title
        self.band_name : str = band_name
        # vote for and againt
        self.votes : int = 0
    
    @property
    def fullname(self) -> str:
        """name of song and band"""
        return f"{self.title} by {self.band_name}"
    
    def set_ID(self, ID : int) -> None:
        self.ID = ID

    def __repr__(self) -> str:
        return f"Song : ID : {self.ID}, {self.fullname}, {self.votes} vote(s)" 