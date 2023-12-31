import sqlite3
import datetime

# understood
def create_table(cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS productivity (
                        date TEXT,
                        time INTEGER,
                        rate INTEGER,
                        tasks TEXT)''')

# understood
def insert_record(cursor, date, hour, rate, tasks):
    cursor.execute('''INSERT INTO productivity (date, time, rate, tasks) VALUES (?, ?, ?, ?)''', (date, hour, rate, tasks))

# understood
def get_average_productivity(cursor, date):
    cursor.execute('''SELECT AVG(rate) FROM productivity WHERE date = ?''', (date,))
    result = cursor.fetchone()
    return result[0] if result[0] is not None else None

# understood
def record_productivity(cursor, date):
    for hour in range(7, 22):
        time_label = f"{hour % 12 if hour != 12 else 12} {'PM' if hour >= 12 else 'AM'}"
        tasks = input(f"\nWhat did you do until {time_label}?: ").strip()

        while True:
            try:
                rate = int(input("\nRate your productivity [1-10]: "))
                if 1 <= rate <= 10:
                    insert_record(cursor, date, hour, rate, tasks)
                    break
                else:
                    print("Please enter a number between 1 and 10.")
            except ValueError:
                print("Invalid input. Please enter a number.")

# understood
def main():
    conn = sqlite3.connect('MyHistory.db')
    cursor = conn.cursor()
    create_table(cursor)

    today = datetime.datetime.now().strftime("%Y-%m-%d")

    while True:
        choice = input("\nSelect number |Record today [1]| Result today [2]| Exit [3]: ")
        if choice == '1':
            record_productivity(cursor, today)
        elif choice == '2':
            average = get_average_productivity(cursor, today)
            if average is not None:
                print(f"Average productivity rate for today is {average:.2f}")
            else:
                print("No productivity data available for today.")
        elif choice == '3':
            break
        else:
            print("Invalid input, please try again.")

    conn.commit()
    conn.close()

# understood
if __name__ == "__main__":
    main()