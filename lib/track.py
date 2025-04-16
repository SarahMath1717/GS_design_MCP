class Track:

    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    def format(self):
        track = f"{self.title} by {self.artist}"
        pass