from library import Book, Member, Library

def main():
    library = Library("My Library")

    while True:
        print("\n===== Library Menu =====")
        print("1. Add Book")
        print("2. Add Member")
        print("3. Show Books")
        print("4. Show Members")
        print("5. Borrow Book")
        print("6. Return Book")
        print("7. Exit")

        choice = input("Enter choice (1-7): ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            isbn = input("Enter book ISBN: ")
            book = Book(title, author, isbn)
            library.add_book(book)

        elif choice == "2":
            name = input("Enter member name: ")
            member_id = input("Enter member ID: ")
            member = Member(name, member_id)
            library.add_member(member)

        elif choice == "3":
            library.show_books()

        elif choice == "4":
            library.show_members()

        elif choice == "5":
            member_id = input("Enter member ID: ")
            title = input("Enter book title: ")

            member = next((m for m in library.members if m.member_id == member_id), None)
            book = library.find_book(title)

            if member and book:
                member.borrow_book(book)
            else:
                print("Member or book not found.")

        elif choice == "6":
            member_id = input("Enter member ID: ")
            title = input("Enter book title: ")

            member = next((m for m in library.members if m.member_id == member_id), None)
            book = library.find_book(title)

            if member and book:
                member.return_book(book)
            else:
                print("Member or book not found.")

        elif choice == "7":
            print("Exiting program... Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
