from db_manager import BookManager

def main_menu(book_manager):
    while True:
        print("-----------------------------------------------")
        print("----- Приложение для управления книгами -----")
        print("1. Добавить книгу")
        print("2. Просмотреть список всех книг")
        print("3. Поиск книг")
        print("4. Удалить книгу")
        print("5. Выйти из приложения")

        choice = input("Введите номер действия: ")

        match choice:
            case "1":
                # Добавление книги
                title = input("Введите название книги: ")
                author = input("Введите имя автора: ")
                description = input("Введите описание книги: ")
                genre = input("Введите жанр книги: ")
                book_manager.add_book(title, author, description, genre)
            case "2":
                # Просмотр списка всех книг
                book_manager.display_all_books()
            case "3":
                # Поиск книг
                keyword = input("Введите ключевое слово: ")
                book_manager.search_books(keyword)
            case "4":
                # Удаление книги
                book_id = int(input("Введите ID книги: "))
                book_manager.delete_book(book_id)
            case "5":
                # Выход из приложения
                break
            case _:
                print("Неверный выбор. Попробуйте еще раз.")

if __name__ == "__main__":
    db_file = "books.db"
    book_manager = BookManager(db_file)
    main_menu(book_manager)
    book_manager.close_connection()