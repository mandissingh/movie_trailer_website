import webbrowser


class Movies():
    """
        This class provides a way to solve to store
        movie related information
        title : indicates title of movie
        rating : indicates dynamic rating shown for movie
        trailer_youtube_url : indicates link of respective movie trailer url
        poster_image_url : indicates link of respective movie poster url
        storyline : brief decription of movie """

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    # Constructor For Movie Class

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.trailer_youtube_url = trailer_youtube
        self.poster_image_url = poster_image
        self.storyline = movie_storyline

    # Open the Youtube trailer of Specified Movie

    def show_trailer(self):
        webbrowser.open(self.trailer)
