class Book:
    def __init__(self, title, author, pages, genre, volume=1):  # Set volume to 1 by default
        self.title = title
        self.author = author
        self.pages = pages
        self.genre = genre
        self.volume = volume

    def __str__(self):
        return f"{self.title} by {self.author} (Volume {self.volume})"  # Include volume information

    def __len__(self):
        return self.pages

    def __del__(self):
        print(f"{self.title} (Volume {self.volume}) has been deleted")  # Include volume information


# Create book objects with corrected arguments and volume handling
book1 = Book("The Moon Also Sets", "John Doe", 300, "Fiction")
book2 = Book("First Blood", "David Morrell", 220, "Thriller")  # Corrected author
book3 = Book("No More Mr. Nice Guy", "Robert L", 400, "Self-Help", 2)  # Explicit volume

print(book1)  # Output: The Moon Also Sets by John Doe (Volume 1)
print(book2)  # Output: First Blood by David Morrell (Volume 1)
print(book3)  # Output: No More Mr. Nice Guy by Robert L (Volume 2)
