"""A video playlist class."""


class Playlist:
    """A class used to represent a Playlist."""

    def __init__(self):
        self._collection = {}
        
    def name_existed(self, playlist_name_underline):
        if playlist_name_underline.lower() in str(self._collection.keys()).lower():
            return True
        else:
            return False
        
    def get_underline_name(playlist_name):
        return playlist_name.replace(" ", "_")
        
    def create_playlist(self, playlist_name):
        playlist_name_underline = self.get_underline_name(playlist_name)
        
        name_existing = self.name_existed(playlist_name_underline)
        
        if not name_existing:
            self._collection[playlist_name_underline] = ()
            print("Successfully created new playlist: {}".format(playlist_name_underline))
        else:
            print("Cannot create playlist: A playlist with the same name already exists")
            
            
    def add_to_playlist(self, playlist_name, video_id):
        playlist_name_underline = self.get_underline_name(playlist_name)
        
        name_existing = self.name_existed(playlist_name_underline)
        
        if not name_existing:
            print("Cannot add video to another_playlist: Playlist does not exist")
            
        