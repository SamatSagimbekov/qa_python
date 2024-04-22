import pytest
from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book(self):
        collector = BooksCollector()
        collector.add_new_book('Book 1')
        collector.add_new_book('Book 2')
        assert len(collector.get_books_genre()) == 2

    def test_set_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Book 1')
        collector.set_book_genre('Book 1', 'Fantasy')
        assert collector.get_book_genre('Book 1') == 'Fantasy'

    def test_get_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Book 1')
        collector.set_book_genre('Book 1', 'Fantasy')
        assert collector.get_book_genre('Book 1') == 'Fantasy'
        assert collector.get_book_genre('Nonexistent Book') is None

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Book 1')
        collector.add_new_book('Book 2')
        collector.set_book_genre('Book 1', 'Fantasy')
        collector.set_book_genre('Book 2', 'Fantasy')
        assert collector.get_books_with_specific_genre('Fantasy') == ['Book 1', 'Book 2']

    def test_get_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Book 1')
        collector.set_book_genre('Book 1', 'Fantasy')
        assert collector.get_books_genre() == {'Book 1': 'Fantasy'}

    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Book 1')
        collector.add_new_book('Book 2')
        collector.set_book_genre('Book 1', 'Fantasy')
        collector.set_book_genre('Book 2', 'Horror')
        assert collector.get_books_for_children() == ['Book 1']

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Book 1')
        collector.add_book_in_favorites('Book 1')
        assert collector.get_list_of_favorites_books() == ['Book 1']
        collector.add_book_in_favorites('Book 1')
        assert collector.get_list_of_favorites_books() == ['Book 1']

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Book 1')
        collector.add_book_in_favorites('Book 1')
        collector.delete_book_from_favorites('Book 1')
        assert collector.get_list_of_favorites_books() == []
        collector.delete_book_from_favorites('Nonexistent Book')
        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book('Book 1')
        collector.add_new_book('Book 2')
        collector.add_book_in_favorites('Book 1')
        collector.add_book_in_favorites('Book 2')
        assert collector.get_list_of_favorites_books() == ['Book 1', 'Book 2']

    def test_add_new_book_with_existing_name(self):
        collector = BooksCollector()
        collector.add_new_book('Book 1')
        collector.add_new_book('Book 1')
        assert len(collector.get_books_genre()) == 1

    def test_set_book_genre_for_nonexistent_book(self):
        collector = BooksCollector()
        collector.set_book_genre('Nonexistent Book', 'Fantasy')
        assert collector.get_books_genre() == {}

    def test_add_book_in_favorites_nonexistent_book(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Nonexistent Book')

    def test_delete_book_from_favorites_nonexistent_book(self):
        collector = BooksCollector()
        collector.add_new_book('Book 1')
        collector.add_book_in_favorites('Book 1')
        collector.delete_book_from_favorites('Nonexistent Book')
        assert collector.get_list_of_favorites_books() == ['Book 1']
    def test_add_new_book_max_length_name(self):
        collector = BooksCollector()
        long_name = 'A' * 40
        collector.add_new_book(long_name)
        assert len(collector.get_books_genre()) == 1

    def test_add_new_book_exceed_max_length_name(self):
        collector = BooksCollector()
        long_name = 'A' * 41
        collector.add_new_book(long_name)
        assert len(collector.get_books_genre()) == 0

    def test_set_book_genre_invalid_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Book 1')
        collector.set_book_genre('Book 1', 'Invalid Genre')
        assert collector.get_book_genre('Book 1') == ''
