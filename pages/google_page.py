from playwright.sync_api import Page

class GooglePage:
    def __init__(self, page: Page):
        self.page = page
        self.search_edit = self.page.locator('textarea[name="q"]')

    def navigate(self):
        self.page.goto("https://www.google.com")

    def search(self, query: str):       
        self.search_edit.click()
        self.search_edit.fill(query)
        self.search_edit.press("Enter")