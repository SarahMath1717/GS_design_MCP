from lib.track import *

def test_track_stores_name():
    track = Track ("Always The Hard Way", "Terror")
    assert track.title == "Always The Hard Way"
    assert track.artist == "Terror"
    