import sqlite3
import datetime

def selection():
    while True:
        choice = input("\nSelect number |Record today [1]| Result today [2]|: ")
        if choice == '1':
            execute_main()
            break

        elif choice == '2':
            computing()
            break

        else:
            print("Invalid input, please try again.")

def execute_main():
    


    for hour in range(7, 22):
        time_label = f"{hour % 12 if hour != 12 else 12} {'PM' if hour >= 12 else 'AM'}"
        tasks = input(f"\nWhat did you do until {time_label}?: ").strip()
        c.execute(f'''CREATE TABLE IF NOT EXISTS {now2} (time INTEGER,rate INTEGER,tasks TEXT) ''')
        

        while True:
            try:
                rate = int(input("\nRate your productivity [1-10]: "))
                if 1 <= rate <= 10:
                    c.execute(f'''INSERT INTO {now2} VALUES ({hour},{rate},"{tasks}")''')
                    conn.commit()
                    break

                else:           
                    print("Please enter a number between 1 and 10.")

            except ValueError:
                print("Invalid input. Please enter a number.")


def computing():

    try:
        average = 0
        j = 0
        for row in c.execute(f'''SELECT rate FROM {now2}'''):
            j+=1
            for i in row:
                average +=i           

        if row:
            average /= j 
            print(f"Average productivity rate for today is {average:.2f}")

        else:
            print("No productivity data available for today.")

    except KeyError:
        print("No data available for today.")


now = {datetime.datetime.now().strftime("%Y-%m-%d")}
now2 = f"\"{now}\""

conn = sqlite3.connect('MyHistory.db')
c = conn.cursor()

selection()

conn.close()
