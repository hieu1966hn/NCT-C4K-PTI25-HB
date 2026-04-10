from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from SS4.models.movie_list import MovieList


def build_sample_movie_list():
    movie_list = MovieList()

    samples = [
        {
            "title": "Naruto",
            "release_date": "Oct 2002",
            "image": "naruto.jpg",
            "rating": 8.4,
            "link": "https://example.com/naruto",
        },
        {
            "title": "One Piece",
            "release_date": "Oct 1999",
            "image": "onepiece.jpg",
            "rating": 8.9,
            "link": "https://example.com/onepiece",
        },
        {
            "title": "Demon Slayer",
            "release_date": "Apr 2019",
            "image": "demonslayer.jpg",
            "rating": 8.6,
            "link": "https://example.com/demonslayer",
        },
    ]

    for movie in samples:
        movie_list.add_item(movie)

    return movie_list


def run_tests():
    movie_list = build_sample_movie_list()

    print("1. Test add_item")
    assert len(movie_list.movie_item_list) == 3
    assert movie_list.movie_item_list[0].movie_id == 0
    assert movie_list.movie_item_list[1].movie_id == 1
    assert movie_list.movie_item_list[2].movie_id == 2
    print("OK")

    print("2. Test get_first_item_by_title")
    found = movie_list.get_first_item_by_title("One Piece")
    assert found is not False
    assert found.title == "One Piece"
    assert movie_list.get_first_item_by_title("Conan") is False
    print("OK")

    print("3. Test search_by_title")
    results = movie_list.search_by_title("piece")
    assert len(results) == 1
    assert results[0].title == "One Piece"
    results = movie_list.search_by_title("NAR")
    assert len(results) == 1
    assert results[0].title == "Naruto"
    print("OK")

    print("4. Test edit_item")
    movie_list.edit_item(
        "Naruto",
        {
            "rating": 9.0,
            "link": "https://new.example.com/naruto",
        },
    )
    naruto = movie_list.get_first_item_by_title("Naruto")
    assert naruto.rating == 9.0
    assert naruto.link == "https://new.example.com/naruto"
    print("OK")

    print("5. Test sort_item_by_rating")
    top_rating = movie_list.sort_item_by_rating(top=0)
    assert top_rating.title == "Naruto"
    assert [movie.title for movie in movie_list.movie_item_list] == [
        "Naruto",
        "One Piece",
        "Demon Slayer",
    ]
    print("OK")

    print("6. Test sort_item_by_title")
    top_title = movie_list.sort_item_by_title(top=0)
    assert top_title.title == "Demon Slayer"
    assert [movie.title for movie in movie_list.movie_item_list] == [
        "Demon Slayer",
        "Naruto",
        "One Piece",
    ]
    print("OK")

    print("7. Test sort_item_by_date")
    newest = movie_list.sort_item_by_date(top=0)
    assert newest.title == "Demon Slayer"
    assert [movie.title for movie in movie_list.movie_item_list] == [
        "Demon Slayer",
        "Naruto",
        "One Piece",
    ]
    print("OK")

    print("8. Test delete_item")
    movie_list.delete_item("One Piece")
    assert len(movie_list.movie_item_list) == 2
    assert [movie.title for movie in movie_list.movie_item_list] == [
        "Demon Slayer",
        "Naruto",
    ]
    print("OK")

    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
