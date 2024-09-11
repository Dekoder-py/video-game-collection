from .database_connection import DatabaseConnection


def create_game_table():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('CREATE TABLE IF NOT EXISTS games(name text primary key, publisher text, finishable integer, read integer)')


def add_game(name: str, pub: str) -> None:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('INSERT INTO games VALUES(?, ?, 1, 0)', (name, pub))


def get_all_games():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM games')
        games = [{'name': row[0], 'publisher': row[1], 'can be finished': row[2], 'read': row[3]}
                 for row in cursor.fetchall()]
    return games


def mark_as_finished(name):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('UPDATE games SET read = 1 WHERE name = ?', (name,))
        cursor.execute('UPDATE games SET finishable = 1 WHERE name = ?', (name,))


def delete_book(name):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('DELETE FROM games WHERE name = ?', (name,))


def game_cannot_be_completed(name):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('UPDATE games SET finishable = 0 where name = ?', (name, ))
