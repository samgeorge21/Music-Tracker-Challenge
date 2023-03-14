class MusicTracker():
    def __init__(self):
        self._music = []
        # Parameters:
        #   self: representing current instance

    def add_track(self, track):
        if not isinstance(track, str):
            raise Exception("This is not a music track and cannot be added to the tracker")
        if track in self._music:
            print(f"{track} is already in the list.")
        else:
            self._music.append(track)
            print(f"{track} has been added to the list.")
            return self._music
        # appends to music list
        # include error message for non-strings
        # include check for if track has already been added to list, preventing it from being added again
        # Parameters:
        #   track: string, representing tracks listened to

    def listened_to(self):
        print("Current list: ")
        for track in self._music:
            print(track)
        return self._music
        # return the music list
        # Returns:
        #  A list, updated with tracks listened to