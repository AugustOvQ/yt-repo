"""A video player class."""

import random
from .video_library import VideoLibrary
from .video_playlist import Playlist


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self._video_playlist = Playlist()

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        print("Here's a list of all available videos:")
        all_videos = []
        for video in self._video_library.get_all_videos():
            tags = ' '.join(video.tags)
            all_videos.append(
                video.title + " (" + video.video_id + ") " + '[' + tags + ']')
        all_videos.sort()
        for video in all_videos:
            print(video)

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        target = self._video_library.get_video(video_id)
        if target == None:
            print("Cannot play video: Video does not exist")
        else:
            for video in self._video_library.get_all_videos():
                if video.get_play():
                    print("Stopping video: {}".format(video.title))
                    # if target != video:
                    video.play()
                    break
            print("Playing video: {}".format(target.title))
            target.play()

    def stop_video(self):
        """Stops the current video."""
        video_playing = False
        for video in self._video_library.get_all_videos():
            if video.get_play():
                print("Stopping video: {}".format(video.title))
                video.play()
                video_playing = True
                break
        if not video_playing:
            print("Cannot stop video: No video is currently playing")

    def play_random_video(self):
        """Plays a random video from the video library."""
        random_video = random.choice(self._video_library.get_all_videos())
        self.play_video(random_video.video_id)

    def pause_video(self):
        """Pauses the current video."""
        video_pausing = False
        for video in self._video_library.get_all_videos():
            if video.get_play():
                if video.get_pause() == False:
                    print("Pausing video: {}".format(video.title))
                    video.pause()
                else:
                    print("Video already paused: {}".format(video.title))
                video_pausing = True
                break
        if not video_pausing:
            print("Cannot pause video: No video is currently playing")

    def continue_video(self):
        """Resumes playing the current video."""
        video_contunuing = False
        for video in self._video_library.get_all_videos():
            if video.get_play():
                if video.get_pause() == False:
                    print("Cannot continue video: Video is not paused")
                else:
                    print("Continuing video: {}".format(video.title))
                    video.pause()
                video_contunuing = True
                break
        if not video_contunuing:
            print("Cannot continue video: No video is currently playing")

    def show_playing(self):
        """Displays video currently playing."""
        video_showing = False
        for video in self._video_library.get_all_videos():
            if video.get_play():
                paused = ""
                if video.get_pause():
                    paused = " - PAUSED"
                tags = ' '.join(video.tags)
                print("Currently playing: " + video.title + " (" + video.video_id + ") " +
                      '[' + tags + ']' + paused)
                video_showing = True
                break
        if not video_showing:
            print("No video is currently playing")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        
        self._video_playlist.create_playlist(playlist_name)

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        
        print("gg")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
