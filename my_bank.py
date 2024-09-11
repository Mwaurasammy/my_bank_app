import sqlite3


def create_database_table():  # Creates table and connects db
    with sqlite3.connect("my_bank.db") as db_connection:
        db_cursor = db_connection.cursor()
        db_cursor.execute("""
            CREATE TABLE IF NOT EXISTS bank_users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                owners_name TEXT NOT NULL,
                location TEXT NOT NULL,
                account_number INTEGER NOT NULL UNIQUE
            )
        """)  # Creates table
        db_connection.commit()


class BankApplication:
    def __init__(self, owners_name, location, account_number):
        self.owners_name = owners_name
        self.location = location
        self.account_number = account_number

    def __str__(self):
        return f"Account for {self.owners_name} has been successfully created and account number is {self.account_number}"


def main():
    create_database_table()
    print("Welcome to my bank!")

    while True:
        print("Menu options:")
        print("1. Create an account")
        print("2. Exit")

        menu_options = input("Choose from menu options: ")

        if menu_options == "1":
            owners_name = input("Enter your full name: ")
            location = input("Enter your location: ")
            account_number = input("Enter account number: ")

            with sqlite3.connect("my_bank.db") as db_connection:
                db_cursor = db_connection.cursor()
                db_cursor.execute("SELECT * FROM bank_users WHERE account_number = ?", (account_number,))
                results = db_cursor.fetchone()

                if results:
                    print("Account already exists!!")
                else:
                    db_cursor.execute("INSERT INTO bank_users (owners_name, location, account_number) VALUES(?, ?, ?)", (owners_name, location, account_number))
                    db_connection.commit()
                    print(f"Account for {owners_name} has been successfully created and account number is {account_number}")

        elif menu_options == "2":
            break
        else:
            print("Invalid choice, please try again!")


if __name__ == "__main__":
    main()
