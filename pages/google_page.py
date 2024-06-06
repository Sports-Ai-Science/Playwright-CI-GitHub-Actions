from playwright.sync_api import Page

class GooglePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self):
        self.page.goto("https://www.google.com")

    def search(self, query: str):
        self.page.get_by_label("検索", exact=True).click()
        self.page.get_by_label("検索", exact=True).fill(query)
        self.page.get_by_label("検索", exact=True).press("Enter")