"""
Handle the requests to the artist endpoint
"""


class Artists:
    """
    Wraps the spotify artist functions
    """

    def __init__(self, api):  # :type async_spotify.API
        self.api = api  # :type async_spotify.API

    def get_artist(self, artist_id: str):
        """
        Get the artist by id

        Args:
            artist_id: The artist id

        Note:
            [https://developer.spotify.com/documentation/web-api/reference/artists/get-artist/](https://developer.spotify.com/documentation/web-api/reference/artists/get-artist/)

        Returns:
            The json associated with the artist
        """

        pass
