class Book:
    """
    A class representing a book with title, author, and publication year.
    Demonstrates the use of Python magic methods.
    """

    def __init__(self, title: str, author: str, year: int):
        """
        Constructor method that initializes the Book instance.
        """
        self.title = title
        self.author = author
        self.year = year

    def __str__(self) -> str:
        """
        Returns a user-friendly string representation of the Book.
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self) -> str:
        """
        Returns the official string representation of the Book.
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"

    def __del__(self):
        """
        Destructor method called when the object is deleted.
        """
        print(f"Deleting {self.title}")