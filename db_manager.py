import sqlite3

class BookManager:
    def __init__(self, db_file):
        # Создаем подключение к базе данных
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

        # Создаем таблицу, если она не существует
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS books
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                            title TEXT,
                            author TEXT,
                            description TEXT,
                            genre TEXT)''')

    def add_book(self, title, author, description, genre):
        #Добавление новой книги#
        self.cursor.execute("INSERT INTO books (title, author, description, genre) VALUES (?, ?, ?, ?)", (title, author, description, genre))
        self.conn.commit()
        print("Книга добавлена в базу данных.")

    def display_all_books(self):
        #Вывод списка всех книг#
        self.cursor.execute("SELECT * FROM books")
        books = self.cursor.fetchall()

        if not books:
            print("Список книг пуст.")
        else:
            print("Список книг:")
            for book in books:
                print("ID:", book[0])
                print("Название:", book[1])
                print("Автор:", book[2])
                print("---------------------------")

    def search_books(self, keyword):
        #Поиск книг по ключевому слову
        self.cursor.execute("SELECT * FROM books WHERE title LIKE ? OR author LIKE ?",
        ('%' + keyword + '%', '%' + keyword + '%'))
        books = self.cursor.fetchall()

        if not books:
            print("Книги не найдены.")
        else:
            print("Результаты поиска:")
            for book in books:
                print("ID:", book[0])
                print("Название:", book[1])
                print("Автор:", book[2])
                print("---------------------------")

    def get_book_by_id(self, book_id):
        #Получение информации о книге по ID
        self.cursor.execute("SELECT * FROM books WHERE id = ?", (book_id,))
        book = self.cursor.fetchone()

        if not book:
            print("Книга не найдена.")
        else:
            return book

    def delete_book(self, book_id):
        #Удаление книги по ID
        self.cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
        self.conn.commit()
        print("Книга удалена из базы данных.")

    def close_connection(self):
        #Закрытие соединения с базой данных
        self.conn.close()
        print("Соединение с базой данных закрыто.")
