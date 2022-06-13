import pytest
from pages import login_page


@pytest.fixture
def login(driver):
    return login_page.LoginPage(driver)


def test_valid_credentials(login):
    login.with_("luism", "123")
    assert login.success_message_present()


def test_invalid_credentials(login):
    login.with_("tomsmith", "bad password")
    assert login.failure_message_present()
