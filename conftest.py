import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language")

@pytest.fixture(scope="function")
def browser(request):
    options = Options()
    browser_language = request.config.getoption("language")
    support_lang = ['es', 'pl', 'ar', 'ca', 'cs', 'da', 'de', 'en-gb', 'el', 'fi', 'fr', 'it', 'ko', 'nl', 'pt', 'pt-br', 'ro', 'ru', 'sk', 'uk', 'zh-hans']
    if browser_language in support_lang:
        options.add_experimental_option('prefs', {'intl.accept_languages': browser_language})
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("--language should be support language")
    yield browser
    print("\nquit browser..")
    browser.quit()
