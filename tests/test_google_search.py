import pytest
from playwright.sync_api import Page
from pages.google_page import GooglePage

def test_google(page: Page):
    google_page = GooglePage(page)
    google_page.navigate()
    
    assert "https://www.google.com/" == page.url


def test_google_search(page: Page):
    google_page = GooglePage(page)
    google_page.navigate()
    google_page.search("Playwright Python２")
    
    assert "https://www.google.com/serch?" in page.url
