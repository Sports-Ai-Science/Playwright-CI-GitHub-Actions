import pytest
from playwright.sync_api import Page
from pages.google_page import GooglePage

def test_google_search(page: Page):
    google_page = GooglePage(page)
    google_page.navigate()
    google_page.search("Playwright Python")
    assert "Playwright Python - Google 検索" == page.title()
