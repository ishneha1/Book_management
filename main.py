books=[]


def list_books():
    return (books)

    
def add_book(name,author,price,p_year):
    book={
        "name": name,
        "author":author,
        "price_npr":price,
        "published_year": p_year
    }
    books.append(book)
    return True


def get_book(name):
    for book in books:
        if book["name"]==name:
            return book
        

def edit_book(name,key_to_edit,new_value):
    for book in books:
        if book["name"]==name:
            book[key_to_edit]=new_value
            return True

        



def main():
    while True:#for infinite loop
        print("Starting book management system......")

        print("enter l for getting book list")
        print("enter n for adding new book")
        print("enter d for book detail")
        print("enter x for deleting book")
        print("enter e for editing book information")
        print("enter q for exiting the application")
        user_input=input("user input:")
        if user_input=="l":
            all_books=list_books()
            print('listing all books')
            for book in all_books:
                print(book)
        elif user_input=="n":
            book_name=input("enter book name:")
            author=input("enter book author:")
            price=int(input(("enter price of book:")))
            published=input('enter book published year:')
            add_book(book_name,author,price,published)

        elif user_input=="d":
            ...
        elif user_input=="x":
            ...
        elif user_input=="e":
            book_name=input('enter book name:')
            book=get_book(book_name)
            print(book)
            key_to_change=input('which information you want to change?')
            new_value=input('enter new value:')


        elif user_input=="q":
            exit()
        else:
            print("your input is invalid")





main()