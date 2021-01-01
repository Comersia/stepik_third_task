import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help='Choose language')

def make_url(language):
    url = 'http://selenium1py.pythonanywhere.com/'
    url += language + '/'
    url += 'catalogue/coders-at-work_207/'
    return url

@pytest.fixture(scope="function")
def url_with_inserting_language(request):
    language_option = request.config.getoption("language")
    print('language', language_option)
    url = make_url(language_option)
    return url

@pytest.fixture(scope="function")
def browser(request):
    print('start browser')
    browser = webdriver.Chrome()
    yield browser
    print('quit browser')
    browser.quit()

