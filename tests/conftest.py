import pytest
from selene import browser
from selenium.webdriver.chrome import options


@pytest.fixture(scope="function", autouse=True)
def browser_open():
    browser.config.base_url = 'https://demoqa.com'
    # browser.config.window_width = 1920
    # browser.config.window_height = 1080
    # options.headless = True

    # yield
    #
    # browser.quit()
