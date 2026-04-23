import allure
from playwright.sync_api import expect,Page
from allureWraper import BasePage


class Loginpage(BasePage):
    def __init__(self, page: Page):
        self.page = page #constructor will also have page characteristics
        self.loginLink=page.locator("//a[@href='/login']")
        self.loginToYourActText=page.locator("//h2[contains(text(),'Login to your account')]")
        self.emailTxtBox=page.locator("//input[@data-qa='login-email']")
        self.passwordTxtBox=page.locator("//input[@data-qa='login-password']")
        self.loginbtn=page.locator("//button[@data-qa='login-button']")

    def clickOnLoginLink(self):
        self.loginLink.click()
        print(self.loginToYourActText)
        expect(self.loginToYourActText).to_be_visible

    def enterEmailID(self,emailValue):
        self.emailTxtBox.fill(emailValue)

    def enterPassword(self,passwordValue):
        self.passwordTxtBox.fill(passwordValue)

    def clickOnLoginBtn(self):
        self.loginbtn.click()

    



     




        

