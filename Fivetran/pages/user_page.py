from pages.base_page import BasePage

class UserPage(BasePage):
    def create_user_table(self):
        query = """
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                username VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL
            )
        """
        self.execute_query(query)

    def insert_user(self, username, email):
        query = f"INSERT INTO users (username, email) VALUES ('{username}', '{email}')"
        self.execute_query(query)

    def get_user_count(self):
        self.db_cursor.execute("SELECT COUNT(*) FROM users")
        return self.db_cursor.fetchone()[0]
