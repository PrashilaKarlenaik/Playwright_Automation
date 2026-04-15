import pytest
from playwright.sync_api import sync_playwright
from Pages.homePage import Homepage
from Pages.loginPage import Loginpage


@pytest.fixture(scope="session")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=3000)
        page = browser.new_page()
        yield page
        browser.close()

#Instead of creating object for every class in testcase, we can create object as a fixture in conftest
#and add this as a paramter in testcase
@pytest.fixture()
def home_Page(page):
    home_Page = Homepage(page)
    return home_Page
            
def login_Page(page):
    login_Page=Loginpage(page)
    return login_Page