# libraries imported
import datetime
import sys
import argparse
import random


# def intro():
#     print(f'Hello Admin {arg.adminName.capitalize()}\nI hope you have a good day today 😊')

# parser = argparse.ArgumentParser(
#     prog='Admin info',
#     description='Store info for the Admin user',
    
# )

# parser.add_argument(
#     '-u', '--adminName' , metavar='adminName',
#     required=True , help='I want to get the user or the admins name'
# )

# arg = parser.parse_args()




#class that represents books
class Book():
    # intro()
    def __init__(self, title , author , year_of_publication, book_id):
        self.title = title
        self.author = author
        self.year_of_publication = year_of_publication
        self.book_id = book_id

    def book_info(self):
        print(f'The book {self.title.capitalize()} was publish by {self.author.capitalize()} in the year {self.year_of_publication}')

    def calculateBookAge(self):
        today = datetime.date.today()
        current_year = today.year
        years_since_published = current_year - self.year_of_publication
        print(f'It has been {years_since_published} years since the book was published')

    def updateAuthor(self):
        is_valid = True
        while is_valid:
            new_author = input(f'Enter a new author for the book {self.title}....')
            if new_author != self.author:
                self.author = new_author
                print(f'Yay you successfully reset the author of the book {self.title} to {new_author.capitalize()}')
                is_valid = False
            else:
                is_valid = True
                print('Please type a valid book author.....')
                # continue

    def get_the_author(self):
        print(f'the new name of the book {self.title} is {self.author.capitalize()}')

    def updatePublicationYear(self):
        is_valid = True
        while is_valid:
            newPublishedBookYear = int(input(f'Enter a new year in the form YYYY for the book {self.title}..'))
            if newPublishedBookYear > datetime.date.today().year:
                is_valid = True
                print('Brother you are looking way far into the future..\ntry again..')
            
            elif newPublishedBookYear < 1500:
                print('This book is too old\nThrow them away')
                sys.exit(0)
            else:
                self.year_of_publication = newPublishedBookYear
                print(f'You successfully reset the year of the book {self.title} to {self.year_of_publication}')
                is_valid = False
            

#class that represents library
class Library(Book):
    def __init__(self):
        #the super constructor inherits the parameters from the parent class which is the Book class
        super().__init__("title", "author", 0, "fe9383838")
        # self.book_id = book_id
        self.library_books = []

    def User_addbooks(self):
        self.title = input('Enter the author of the new book..').capitalize()
        self.author = input('Enter the name of the person who published the book..').capitalize()
        print(' ')
        print(f'You are going to enter the year of when the book was published\nIt shouldn\'t be a year after {datetime.date.today().year}..\nIt shouldn\'t be before the year 1500..')
        self.year_of_publication = input('Enter the year of when the book was published..')

        desired_id_range = 7
        my_radoms = random.randint(10**(desired_id_range - 1) , 10**desired_id_range - 1)
        self.book_id = self.title[0:2].upper() + str(my_radoms)

        my_new_books = {
            "Book title " : self.title,
            "Book Author " : self.author,
            "Year Of Publication" : self.year_of_publication,
            "Book ID" : self.book_id
        }
        # my_new_books = Book(self.title, self.author, self.year_of_publication, self.book_id)
        self.library_books.append(my_new_books)
        print(f'You successfully added the book {self.title} to the library books and these are the information regarding it\n{my_new_books}')

    def list_all_books(self):
        print('These are the books which are currently available in the library\n')
        print(' ')
        if not self.library_books:
         print('There are no books in the library.')
        else:
            for book in self.library_books:
                print(f'{book}\n')

    def remove_book(self):
        print('So you want to remove a book from the library right..cool')
        print(' ')
        user_book_id = input('enter the id of the book you want to remove..')
        for book in self.library_books:
            if user_book_id == book["Book ID"]:
                print('this book id matches our records..\nDo you still want to remove it from the library..')
                print('Press Y for Delete\nPress N for a change of mind..')
                user_confirmation = input('Enter your y or n for confirmation..').lower()
                if user_confirmation == "y":
                    self.library_books.remove(book)
                    print('Book has been successfully removed from the library')
                elif user_confirmation == 'n':
                    print('You decided not to remove the book, so we kept it 😁')
                else:
                    print('I guess your decision was out of range..')
            else:
                print('the book you are searching for is not in this library')

    def Update_author_inlibrary(self):
        user_book_confirmation = input('Please enter the ID of the book you would like alter its author..')
        for book in self.library_books:
            if user_book_confirmation == book["Book ID"]:
                self.updateAuthor()
            else:
                print('The book entered is not matching our records..')

    def Update_published_year(self):
        user_book_search = input('enter the ID of the book you are looking for...')
        for book in self.library_books:
            if user_book_search == book["Book ID"]:
                self.updatePublicationYear()
            else:
                print('the id you entered does not match our records')


    

                

book_1 = Library()
book_1.User_addbooks()
book_1.list_all_books()
book_1.Update_author_inlibrary()
book_1.Update_published_year()

















