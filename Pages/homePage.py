from playwright.sync_api import expect,Page

class Homepage:
    def __init__(self, page: Page):
        self.page = page #constructor will also have page characteristics
        self.homeLink = page.locator("//a[.//i[contains(@class,'fa-home')]]")

    def launchAutomationExercisePage(self):
        self.page.goto("https://automationexercise.com/")
        self.homeLink.click()
        expect(self.homeLink).to_contain_text("Home")       