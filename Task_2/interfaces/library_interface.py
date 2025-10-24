from abc import ABC, abstractmethod
from typing import List
from models.book import Book


class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, book: Book) -> None:
        pass

    @abstractmethod
    def remove_book(self, title: str) -> None:
        pass

    @abstractmethod
    def list_books(self) -> List[Book]:
        pass
