import pytest
from selene.support.shared import browser


@pytest.fixture(scope='function', autouse=True)
def set_window_size():
    browser.config.window_width = 1024
    browser.config.window_height = 1366


@pytest.fixture(scope='function', autouse=True)
def open_browser(set_window_size):
    base_url = 'https://google.com/ncr'
    browser.open(base_url)


