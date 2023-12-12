class BasePage:
    def __init__(self, db_cursor):
        self.db_cursor = db_cursor

    def execute_query(self, query):
        self.db_cursor.execute(query)
        self.db_cursor.connection.commit()
