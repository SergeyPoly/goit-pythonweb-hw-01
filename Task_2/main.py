from services.library import Library
from services.library_manager import LibraryManager
from utils.logger import logger


def main() -> None:
    library = Library()
    manager = LibraryManager(library)

    while True:
        command = input("\nEnter command (add, remove, show, exit): ").strip().lower()

        match command:
            case "add":
                title = input("Enter book title: ").strip()
                author = input("Enter book author: ").strip()
                try:
                    year = int(input("Enter book year: ").strip())
                except ValueError:
                    logger.warning("Year must be a number.")
                    continue
                manager.add_book(title, author, year)
            case "remove":
                title = input("Enter book title to remove: ").strip()
                manager.remove_book(title)
            case "show":
                manager.show_books()
            case "exit":
                break
            case _:
                logger.warning("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
