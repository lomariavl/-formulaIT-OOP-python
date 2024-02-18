class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        return self._name

    @property
    def author(self) -> str:
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """ Класс бумажных книг. """
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, value: int) -> None:
        if not isinstance(value, int):
            raise ValueError("Pages must be an integer.")
        if value <= 0:
            raise ValueError("Pages must be a positive integer.")
        self._pages = value

    def __str__(self):
        return f'PaperBook "{self.name}" by {self.author}, {self.pages} pages'

    """
    Перегружать класс PaperBook методом __repr__ имеет смысл, когда необходимо расширить метод и знать поле pages
    Пример использования:
    >>> example_book = PaperBook("Hearts of Tree", "Jack London", 350)
    >>> copy_book = eval(example_book.__repr__())
    """
    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"


class AudioBook(Book):
    """ Класс аудиокниг. """
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, value: float) -> None:
        if not isinstance(value, float):
            raise ValueError("Duration must be a float.")
        if value <= 0:
            raise ValueError("Duration must be a positive float.")
        self._duration = value

    def __str__(self):
        return f'AudioBook "{self.name}" by {self.author}, duration: {self.duration} hours'

    """
    Перегружать класс AudioBook методом __repr__ имеет смысл, когда необходимо расширить метод и знать поле duration
    Пример использования:
    >>> example_book = AudioBook("Hearts of Tree", "Jack London", 350)
    >>> copy_book = eval(example_book.__repr__())
    """
    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"


book = Book("Hearts of Tree", "Jack London")
print(book.__str__())
print(book.__repr__(), "\n")
paper_book = PaperBook("What Dreams May Come", "Richard Burton Matheson", 540)
audio_book = AudioBook("Genetic", "Martin Moder", 50.2)
print(paper_book.__str__())
print(paper_book.__repr__(), "\n")
print(audio_book.__str__())
print(audio_book.__repr__())

# example_book = PaperBook("Hearts of Tree", "Jack London", 350)
# print(example_book, "\n")
# copy_book = eval(example_book.__repr__())
# print(copy_book)
