from lib.track_list import MusicTracker

# """
# Initially, no music has been listened to
# """

# def test_initially_no_tracks():
#     tracker = MusicTracker()
#     assert tracker.listened_to() == []

# """
# When a track has been listened to
# It is reflected in the list of tracks that have been listened to
# """

# def test_track_added_to_list():
#     tracker = MusicTracker()
#     tracker.add_track("Three Little Birds")
#     assert tracker.listened_to() == ["Three Little Birds"]

# """
# If non-string data is entered then it will return an error
# """

# def test_added_incorrect_data():
#     tracker = MusicTracker()
#     tracker.add_track(57) # Raises an error "This is not a music track and cannot be added to the tracker"

"""
If a duplicate track is input
It will not be added to the list of tracks listened to
"""

def test_duplicate_track_added():
    tracker = MusicTracker()
    tracker.add_track("Three Little Birds")
    tracker.add_track("Three Little Birds")
    assert tracker.listened_to() == ["Three Little Birds"]