import pytest

from main import BooksCollector
from conftest import horror, fantasy, comedy, detective

class TestBooksCollector:
    #Проверка добавления книг
    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    #Проверка добавления книги с уже существующим названием
    def test_add_new_book_add_existed_book_not_added(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert len(collector.get_books_genre()) == 1

    #Проверка добавления книги с названием длиннее 40 символов и менее 1
    @pytest.mark.parametrize('book_name', ['Жизнь, необыкновенные и удивительные приключения Робинзона Крузо', ''])
    def test_add_new_book_add_not_valid_len_book_name_not_added(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert len(collector.get_books_genre()) == 0

    #Проверка назначения существующей книге существующего жанра
    def test_set_book_genre_set_exist_genre_for_exist_book_success(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Ужасы'

    #Проверка назначения НЕ существующей книге существующего жанра
    def test_set_book_genre_set_exist_genre_for_not_exist_book_fails(self):
        collector = BooksCollector()
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        assert len(collector.get_books_with_specific_genre('Ужасы')) == 0

    #Проверка назначения существующей книге НЕ существующего жанра
    def test_set_book_genre_set_not_exist_genre_for_not_exist_book_fails(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Роман')
        assert len(collector.get_books_with_specific_genre('Ужасы')) == 0

    #Проверка получения жанра существующей книги
    def test_get_book_genre_exist_book_success(self, fill_books):
        assert fill_books.get_book_genre(fantasy) == "Фантастика"

    #Проверка получения жанра НЕ существующей книги
    def test_get_book_genre_not_exist_book_empty_response(self, fill_books):
        assert not fill_books.get_book_genre("Что делать, если ваш кот хочет вас убить")

    #Проверка получения списка книг существующего жанра
    def test_get_books_with_specific_genre_exist_genre_success(self, fill_books):
        assert fill_books.get_books_with_specific_genre('Комедии') == [comedy]

    # Проверка получения списка книг НЕ существующего жанра
    def test_get_books_with_specific_genre_not_exist_genre_empty_list(self, fill_books):
        assert fill_books.get_books_with_specific_genre('Антиутопия') == []

    # Проверка получения пустого списка книг существующего жанра при отсутствии книг
    def test_get_books_with_specific_genre_exist_genre_not_exist_book_empty_list(self):
        collector = BooksCollector()
        assert collector.get_books_with_specific_genre('Детективы') == []

    # Проверка получения списка книг, подходящих детям
    def test_get_books_for_children_success(self, fill_books):
        childrens_books = fill_books.get_books_for_children()
        assert horror not in childrens_books and detective not in childrens_books

    # Проверка добавления существующей книги в избранное
    def test_add_book_in_favorites_exist_book_success_added(self, fill_books):
        fill_books.add_book_in_favorites(detective)
        favorites_books = fill_books.get_list_of_favorites_books()
        assert len(favorites_books) == 3 and detective in favorites_books

    # Проверка добавления не существующей книги в избранное
    def test_add_book_in_favorites_not_exist_book_not_added(self, fill_books):
        fill_books.add_book_in_favorites("О дивный новый мир")
        favorites_books = fill_books.get_list_of_favorites_books()
        assert len(favorites_books) == 2 and "О дивный новый мир" not in favorites_books

    # Проверка добавления уже добавленной книги в избранное
    def test_add_book_in_favorites_already_added_book_not_added(self, fill_books):
        fill_books.add_book_in_favorites(fantasy)
        assert len(fill_books.get_list_of_favorites_books()) == 2

    # Проверка удаления из избранного добавленной ранее книги
    def test_delete_book_from_favorites_added_book_success(self, fill_books):
        fill_books.delete_book_from_favorites(fantasy)
        favorites_books = fill_books.get_list_of_favorites_books()
        assert len(favorites_books) == 1 and fantasy not in favorites_books

    # Проверка удаления из избранного отсутствующей в избранном книги
    def test_delete_book_from_favorites_not_added_book_not_delete(self, fill_books):
        fill_books.delete_book_from_favorites(comedy)
        assert len(fill_books.get_list_of_favorites_books()) == 2