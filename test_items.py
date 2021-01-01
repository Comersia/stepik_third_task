import pytest


class TestAnyLanguageInterface():
    def test_language_inteface(self, url_with_inserting_language, browser):
        browser.get(url_with_inserting_language)
        list_buttons = browser.find_elements_by_css_selector('button.btn-add-to-basket')
        assert len(list_buttons) > 0, 'Такой кнопки не нашлось!!!'

