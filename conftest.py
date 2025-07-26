import pytest
from pytest import fixture
from selene import browser

@pytest.fixture
def set_browser():
    browser.open('https://demoqa.com/automation-practice-form')
    browser.config.window_width = 1450
    browser.config.window_height = 800
    yield
    browser.quit()



