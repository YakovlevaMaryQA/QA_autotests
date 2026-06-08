import pytest
from selene import browser

@pytest.fixture(scope='function')
def setup_browser():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    yield
    browser.quit()

@pytest.fixture(scope='function')
def open_browser(setup_browser):
    browser.open('https://duckduckgo.com/')
