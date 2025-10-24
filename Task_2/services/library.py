from typing import List
from interfaces.library_interface import LibraryInterface
from models.book import Book
from utils.logger import logger


class Library(LibraryInterface):
    def __init__(self) -> None:
        self._books: List[Book] = []

    def add_book(self, book: Book) -> None:
        self._books.append(book)
        logger.info(f"Book '{book.title}' added.")

    def remove_book(self, title: str) -> None:
        for book in self._books:
            if book.title == title:
                self._books.remove(book)
                logger.info(f"Book '{title}' removed.")
                return
        logger.warning(f"Book '{title}' not found.")

    def list_books(self) -> List[Book]:
        return self._books
