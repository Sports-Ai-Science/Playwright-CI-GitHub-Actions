import pytest
from playwright.sync_api import sync_playwright
from pages.google_page.py import GooglePage

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()

def test_google_search(page):
    google_page = GooglePage(page)
    google_page.navigate()
    google_page.search("Playwright Python")
    assert "Playwright Python" in page.title()
