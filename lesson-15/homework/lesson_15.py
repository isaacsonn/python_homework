import sqlite3

def create_database():
    conn = sqlite3.connect('star_trek.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Roster (
        Name TEXT,
        Species TEXT,
        Age INTEGER
    )
    ''')

    crew_members = [
        ('Benjamin Sisko', 'Human', 40),
        ('Jadzia Dax', 'Trill', 300),
        ('Kira Nerys', 'Bajoran', 29)
    ]
    cursor.executemany('INSERT INTO Roster VALUES (?, ?, ?)', crew_members)

    cursor.execute('''
    UPDATE Roster
    SET Name = 'Ezri Dax'
    WHERE Name = 'Jadzia Dax'
    ''')

    conn.commit()
    conn.close()

def display_bajorans():
    conn = sqlite3.connect('star_trek.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    SELECT Name, Age FROM Roster
    WHERE Species = 'Bajoran'
    ''')
    
    bajorans = cursor.fetchall()
    print("\nBajoran Crew Members:")
    for name, age in bajorans:
        print(f"{name}, Age: {age}")
    
    conn.close()

if __name__ == "__main__":
    create_database()
    display_bajorans()
    print("\nDatabase operations completed successfully!")

    conn = sqlite3.connect('star_trek.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Roster')
    print("\nComplete Roster:")
    for row in cursor.fetchall():
        print(row)
    conn.close()
