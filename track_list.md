# Music Track List Class Design Recipe

# 1. DESCRIBE THE PROBLEM:

> As a user
> So that I can keep track of my music listening
> I want to add tracks I've listened to and see a list of them.

# 2. DESIGN CLASS INTERFACE:

...python
class MusicTracker():
    def __init__(self):
        self._music = []
        # Parameters:
        #   self: representing current instance
        pass

    def add_track(self, track):
        # appends to music list
        # include error message for non-strings
        # include check for if track has already been added to list, preventing it from being added again
        # Parameters:
        #   track: string, representing tracks listened to
        pass

    def listened_to(self):
        # return the music list
        # Returns:
        #  A list, updated with tracks listened to
        pass

    # Side-effects:
    #   None expected

# 3. CREATE TEST EXAMPLES:

...python
"""
Initially, no music has been listened to
"""

def test_initially_no_tracks():
    tracker = MusicTracker()
    assert tracker.listened_to() == []

"""
When a track has been listened to
It is reflected in the list of tracks that have been listened to
"""

def test_track_added_to_list():
    tracker = MusicTracker()
    tracker.add_track("Three Little Birds")
    assert tracker.listened_to() == ["Three Little Birds"]

"""
If non-string data is entered then it will return an error
"""

def test_added_incorrect_data():
    tracker = MusicTracker()
    tracker.add_track(57) # Raises an error "This is not a music track and cannot be added to the tracker"

"""
If a duplicate track is input
It will not be added to the list of tracks listened to
"""

def test_duplicate_track_added():
    tracker = MusicTracker()
    tracker.add_track("Three Little Birds")
    tracker.add_track("Three Little Birds")
    assert tracker.listened_to() == ["Three Little Birds"]


# 4. IMPLEMENT BEHAVIOUR:

...python