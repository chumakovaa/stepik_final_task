import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en',
                     help="Choose language")
    parser.addoption('--headless', action='store', default='false',
                     help="Open a browser invisible, without GUI is used by default")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption('language')
    browser_name = request.config.getoption("browser_name")
    headless = request.config.getoption('headless')
    browser = None
    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        if headless == 'true':
            options.add_argument('headless')
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    browser.quit()


