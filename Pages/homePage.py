import allure
from playwright.sync_api import expect,Page
from allureWraper import BasePage

class Homepage(BasePage): #allure report is in baseclass and homepage is inheriting that,so we can use allure step in homepage also without adding @allure.step in homepage
    def __init__(self, page: Page):
        self.page = page #constructor will also have page characteristics
        self.homeLink = page.locator("//a[.//i[contains(@class,'fa-home')]]")

    def launchAutomationExercisePage(self):
        self.page.goto("https://automationexercise.com/")
        self.homeLink.click()
        expect(self.homeLink).to_contain_text("Home")       