import media
import fresh_tomatoes

# Function to get direct information of Movie details like
# title , rating , poster etc.
dangal = media.Movies("Dangal",
                      "Geeta Phogat's life story of winning" +
                      "gold medal for india",
                      "https://images-na.ssl-images-amazon.com" +
                      "/images/M/MV5BMTQ4MzQzMzM2Nl5BMl5BanBnXkFtZTgw" +
                      "MTQ1NzU3MDI@._V1_UY268_CR4,0,182,268_AL__QL50.jpg",
                      "https://www.youtube.com/watch?v=x_7YlGv9u1g"
                      )

avatar = media.Movies("Avatar",
                      "A marine on an alien planet",
                      "https://images-na.ssl-images-amazon.com" +
                      "/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZT" +
                      "cwODc5MTUwMw@@._V1_UX182_CR0,0,182,268_AL__QL50.jpg",
                      "https://www.youtube.com/watch?v=5PSNL1qE6VY"
                      )

three_idiots = media.Movies("3 idiots",
                            "Story of 3 idiots",
                            "https://images-na.ssl-images-amazon.com/images" +
                            "/M/MV5BZWRlNDdkNzItMzhlZC00YTdmLWIwNjktYjY5N" +
                            "jQ1ZmQ3N2FkXkEyXkFqcGdeQXVyNjU0OTQ0OT" +
                            "Y@._V1_UY268_C" +
                            "R9,0,182,268_AL__QL50.jpg",
                            "https://www.youtube.com/watch?v=K0eDlFX9GMc"
                            )

avengers = media.Movies("Avengers",
                        "When earth's mightiest heroes fight against evil",
                        "https://images-na.ssl-images-amazon.com" +
                        "/images/M/MV5BMTk2NTI1MTU4N15BMl5BanBnX" +
                        "kFtZTcwODg0OTY0Nw@@._V1_UX182_CR0,0,182" +
                        ",268_AL__QL50.jpg",
                        "https://www.youtube.com/watch?v=eOrNdBpGMv8"
                        )

the_dark_knight = media.Movies("The Dark Knight",
                               "When batman fight his rival Joker",
                               "https://images-na.ssl-images-amazon." +
                               "com/images/M/MV5BMTMxNTMwODM0NF5BMl5B" +
                               "anBnXkFtZTcwODAyMTk2Mw@@._V1_UX182_CR0" +
                               ",0,182,268_AL__QL50.jpg",
                               "https://www.youtube.com/watch?v=EXeTwQWrcwY")

angrej = media.Movies("Angrej",
                      "The story of Gejja and Dhan Kaur",
                      "https://images-na.ssl-images-amazo" +
                      "n.com/images/M/MV5BOWY2NjJjMjEtNjY2Yy" +
                      "00YjE5LTkzYjctNjBkMDkwMzA1MWY4XkEyXkFqcG" +
                      "deQXVyNTE4ODU0NzA@._V1_UY268_CR177,0,182,268"
                      "+_AL__QL50.jpg",
                      "https://www.youtube.com/watch?v=2jcbSzoPNVA"
                      )

# Array of Movie objects is Created
movies = [angrej, the_dark_knight, avengers, three_idiots, avatar, dangal]
# HTML page is requested
fresh_tomatoes.open_movies_page(movies)
