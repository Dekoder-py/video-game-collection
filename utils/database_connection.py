import sqlite3


class DatabaseConnection:
    def __init__(self, host) -> None:
        self.connection = None
        self.host = host


    def __enter__(self) -> sqlite3.Connection:
        self.connection = sqlite3.connect(self.host)
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        if exc_type or exc_val or exc_tb:
            self.connection.close()
            print('An error occurred and the connection to the database was closed with no commits.')
        else:
            self.connection.commit()
            self.connection.close()
