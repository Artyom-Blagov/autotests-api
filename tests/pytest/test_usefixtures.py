import pytest

@pytest.fixture
def clear_books_database():
    print("[FIXTURE] Удаляем все данные из БД")


@pytest.fixture
def fill_books_database():
    print("[FIXTURE] Создаём новые данные в БД")


class TestLibrary:
    @pytest.mark.usefixtures("clear_books_database", "fill_books_database")
    def test_read_book_from_library(self):
        ...

    @pytest.mark.usefixtures("clear_books_database", "fill_books_database")
    def test_delete_book_from_library(self):
        ...