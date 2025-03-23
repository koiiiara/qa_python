import pytest
from main import BooksCollector

fantasy = 'Колыбель для кошки'
horror = 'Гордость и предубеждение и зомби'
detective = 'Десять негритят'
cartoons = 'Волшебник изумрудного города'
comedy = '12 стульев'

@pytest.fixture(scope="function")
def fill_books():
    collector = BooksCollector()
    books_genre = {
        fantasy: "Фантастика",
        horror: "Ужасы",
        detective: "Детективы",
        cartoons: "Мультфильмы",
        comedy: "Комедии",
    }

    for book, genre in books_genre.items():
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)

    collector.add_book_in_favorites(fantasy)
    collector.add_book_in_favorites(horror)

    return collector