from selene import be, have
from selene.support.shared import browser


def test_positive_search(open_browser):
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_negative_search(open_browser):
    str = 'hghagshaslaks'
    browser.element('[name="q"]').should(be.blank).type(str).press_enter()
    browser.element('[id="topstuff"]').should(have.text(f'Your search - {str} - did not match any documents.'))