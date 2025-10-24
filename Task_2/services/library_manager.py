from interfaces.library_interface import LibraryInterface
from models.book import Book
from utils.logger import logger


class LibraryManager:
    def __init__(self, library: LibraryInterface) -> None:
        self.library = library

    def add_book(self, title: str, author: str, year: int) -> None:
        book = Book(title, author, int(year))
        self.library.add_book(book)

    def remove_book(self, title: str) -> None:
        self.library.remove_book(title)

    def show_books(self) -> None:
        books = self.library.list_books()
        if not books:
            logger.info("No books in the library.")
            return
        logger.info("\n--- Book List ---")
        for book in books:
            logger.info(book)
