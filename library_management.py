class Library:
    def __init__(self):
        self.no_of_books = 0
        self.books = []

    #add single book
    def add_book(self,book_name):
        self.books.append(book_name)
        self.no_of_books +=1

    # Add muntiple books
    def add_muntiple_books(self , book_list):
        self.books.extend(book_list)
        self.no_of_books += len(book_list)

    #methode to show boooks
    def show_books(self):
        print("Books in Library:")
        for book in self.books:
            print(book)
        print("Total Books:" , self.no_of_books)

lib = Library()
#Adding books using different methodes 
lib.add_book("python")
lib.add_book("Java")

lib.add_muntiple_books(["C","DATA STRUCTURES" , "AI BASICS"])
lib.show_books()