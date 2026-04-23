import allure
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

#Hook will monitor the test execution from start to end and if any test fails, it will capture the screenshot and attach it to allure report, its similar to test listeners
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    # Capture screenshots for setup, call, and teardown failures
    if report.failed:
        page = item.funcargs.get("page", None)
        if page:
            step = report.when  # setup / call / teardown
            screenshot = page.screenshot()
            allure.attach(
                screenshot,
                name=f"Failure Screenshot ({step})",
                attachment_type=allure.attachment_type.PNG
            )