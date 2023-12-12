import pytest
from pages.user_page import UserPage

@pytest.fixture(scope="module")
def user_page(db_cursor):
    user_page = UserPage(db_cursor)
    user_page.create_user_table()
    yield user_page

@pytest.mark.parametrize("username, email", [("Alice", "alice@example.com"), ("Bob", "bob@example.com")])
def test_insert_and_count_users(user_page, username, email):
    user_page.insert_user(username, email)
    count = user_page.get_user_count()
    assert count == 1
