class Book:
    def __init__(self,title,author,pages,genre,volume):
        self.title = title
        self.author = author
        self.pages = pages
        self.genre = genre
        self.volume = volume
        
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def __len__(self):
        return self.pages
    
    def __del__(self):
        print(f"{self.title} has been deleted")
        
    #method to get chatper
        
        
        
        
    #create a book object of title: the moon also sets
    book1 = Book("the moon also sets","john Doe", 300, "fiction")
    book2 = Book("first blood")
    book3 = Book("no more mr. nice guy", "Robert L", 400, "self learning")