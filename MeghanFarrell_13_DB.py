import sqlite3
import matplotlib.pyplot as plt


# Create and initialize the database
def create_database():
    conn = sqlite3.connect('population_MF.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS population (
            city TEXT,
            year INTEGER,
            population INTEGER
        )
    ''')
    conn.commit()
    conn.close()


# Insert initial population data for 10 cities in Florida for the year 2023
def insert_initial_data():
    cities = [
        ("Miami", 2023, 442241),
        ("Orlando", 2023, 309154),
        ("Tampa", 2023, 387050),
        ("Jacksonville", 2023, 949611),
        ("Tallahassee", 2023, 199128),
        ("Fort Lauderdale", 2023, 182760),
        ("St. Petersburg", 2023, 265098),
        ("Hialeah", 2023, 238942),
        ("Port St. Lucie", 2023, 217523),
        ("Cape Coral", 2023, 204510)
    ]
    conn = sqlite3.connect('population_MF.db')
    c = conn.cursor()
    c.executemany('INSERT INTO population (city, year, population) VALUES (?, ?, ?)', cities)
    conn.commit()
    conn.close()


# Simulate population growth for the next 20 years at a 2% growth rate
def simulate_population_growth():
    conn = sqlite3.connect('population_MF.db')
    c = conn.cursor()
    for city, year, population in c.execute('SELECT DISTINCT city, year, population FROM population WHERE year = 2023'):
        for i in range(1, 21):
            year += 1
            population = int(population * 1.02)
            c.execute('INSERT INTO population (city, year, population) VALUES (?, ?, ?)', (city, year, population))
    conn.commit()
    conn.close()


# Function to display population growth for a selected city using Matplotlib
def display_population_growth():
    cities = [
        "Miami", "Orlando", "Tampa", "Jacksonville", "Tallahassee",
        "Fort Lauderdale", "St. Petersburg", "Hialeah", "Port St. Lucie", "Cape Coral"
    ]
    print("Choose a city from the following options:")
    for i, city in enumerate(cities):
        print(f"{i + 1}. {city}")
    choice = int(input("Enter the number corresponding to the city: "))
    selected_city = cities[choice - 1]

    conn = sqlite3.connect('population_MF.db')
    c = conn.cursor()
    c.execute('SELECT year, population FROM population WHERE city = ? ORDER BY year', (selected_city,))
    data = c.fetchall()
    conn.close()

    years = [row[0] for row in data]
    populations = [row[1] for row in data]

    plt.figure(figsize=(10, 5))
    plt.plot(years, populations, marker='o')
    plt.title(f'Population Growth for {selected_city}')
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    create_database()
    insert_initial_data()
    simulate_population_growth()
    display_population_growth()8
